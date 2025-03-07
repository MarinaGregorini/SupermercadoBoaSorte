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
    frutas = list(set(p.nome for p in produtos))  # Remove duplicatas

    produtos_por_fruta = {fruta: [p for p in produtos if p.nome == fruta] for fruta in frutas}

    if request.method == 'POST':
        for fruta in frutas:
            produto_selecionado = request.form.get(f'produto_{fruta}')
            if produto_selecionado:
                produto = next((p for p in produtos if p.nome == produto_selecionado), None)
                if produto:
                    consumidor.produtos_selecionados.append(produto)
        return redirect(url_for('resumo_compra'))

    return render_template('escolher_produtos.html', produtos_por_fruta=produtos_por_fruta)

@app.route('/resumo_compra')
def resumo_compra():
    total_poluicao = consumidor.calcular_poluicao_total()
    return render_template('resumo_compra.html', consumidor=consumidor, total_poluicao=total_poluicao)

if __name__ == '__main__':
    app.run(debug=True)
