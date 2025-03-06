from flask import Flask, render_template, request, redirect, url_for
from classes import *

app = Flask(__name__)

consumidor = None

# Rotas
@app.route('/', methods=['GET', 'POST'])
def login():
    global consumidor
    if request.method == 'POST':
        nome = request.form['nome']
        consumidor = Consumidor(nome)
        return redirect(url_for('escolher_produtos'))
    return render_template('login.html')

@app.route('/escolher_produtos', methods=['GET', 'POST'])
def escolher_produtos():
    if request.method == 'POST':
        selecionados = request.form.getlist('produtos')
        for nome_produto in selecionados:
            produto = next((p for p in produtos if p.nome == nome_produto), None)
            if produto:
                consumidor.produtos_selecionados.append(produto)
        return redirect(url_for('resumo_compra'))
    return render_template('escolher_produtos.html', produtos=produtos)

@app.route('/resumo_compra')
def resumo_compra():
    total_poluicao = consumidor.calcular_poluicao_total()
    return render_template('resumo_compra.html', consumidor=consumidor, total_poluicao=total_poluicao)

if __name__ == '__main__':
    app.run(debug=True)
