from flask import Flask, render_template, request, redirect, url_for
from classes import *

app = Flask(__name__)

consumidor = None

@app.route('/', methods=['GET', 'POST'])
def login():
    
    global consumidor
    
    if request.method == 'POST':
        
        nome = (request.form['nome']).title()
        consumidor = Consumidor(nome)
        
        return redirect(url_for('escolher_produtos'))
    
    return render_template('login.html')

@app.route('/escolher_produtos', methods=['GET', 'POST'])
def escolher_produtos():
    
    frutas = list(set(p.nome.split()[0] for p in produtos))
    produtos_por_fruta = {fruta: [p for p in produtos if p.nome.split()[0] == fruta] for fruta in frutas}
    
    produto_recomendado_por_fruta = {
        fruta: min(fornecedores, key=lambda p: p.custo_poluicao)
        for fruta, fornecedores in produtos_por_fruta.items()
    }

    if request.method == 'POST':
        
        consumidor.produtos_selecionados.clear()
        
        for fruta, fornecedores in produtos_por_fruta.items():
            
            for produto in fornecedores:
                
                quantidade = request.form.get(f'quantidade_{produto.nome}', 0)
                quantidade = int(quantidade) 

                if quantidade > 0:
                    consumidor.adicionar_produto(produto, quantidade)
        
        return redirect(url_for('resumo_compra'))
    
    return render_template(
        'escolher_produtos.html', produtos_por_fruta=produtos_por_fruta, produto_recomendado_por_fruta=produto_recomendado_por_fruta
        )

@app.route('/resumo_compra')
def resumo_compra():
    
    total_poluicao = consumidor.calcular_poluicao_total()
    
    return render_template(
        'resumo_compra.html', 
        consumidor=consumidor, 
        total_poluicao=total_poluicao
    )

if __name__ == '__main__':
    app.run(debug=True)