from flask import Flask, render_template, request, redirect, url_for
from models import db, Transportadora, Produtor, Produto, Consumidor, consumidor_produto

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_supermercado.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        consumidor = Consumidor(nome=nome)  # Criando consumidor
        db.session.add(consumidor)
        db.session.commit()  # Salvando no banco

        return redirect(url_for('escolher_produtos', consumidor_id=consumidor.id))  # Redireciona com o ID correto
    
    return render_template('cadastro.html')


@app.route('/escolher_produtos/<int:consumidor_id>', methods=['GET', 'POST'])
def escolher_produtos(consumidor_id):
    consumidor = Consumidor.query.get_or_404(consumidor_id)
    
    produtos = Produto.query.all()
    frutas = list(set(p.nome.split()[0] for p in produtos))
    produtos_por_fruta = {fruta: Produto.query.filter(Produto.nome.startswith(fruta)).all() for fruta in frutas}

    produto_recomendado_por_fruta = {
        fruta: min(fornecedores, key=lambda p: p.custo_poluicao)
        for fruta, fornecedores in produtos_por_fruta.items()
    }

    if request.method == 'POST':
        # Remover produtos antigos do consumidor
        db.session.execute(consumidor_produto.delete().where(consumidor_produto.c.consumidor_id == consumidor.id))

        for fruta, fornecedores in produtos_por_fruta.items():
            for produto in fornecedores:
                quantidade = int(request.form.get(f'quantidade_{produto.id}', 0))
                if quantidade > 0:
                    db.session.execute(consumidor_produto.insert().values(
                        consumidor_id=consumidor.id, produto_id=produto.id, quantidade=quantidade
                    ))

        db.session.commit()
        return redirect(url_for('resumo_compra', consumidor_id=consumidor.id))

    return render_template('escolher_produtos.html', produtos_por_fruta=produtos_por_fruta, produto_recomendado_por_fruta=produto_recomendado_por_fruta, consumidor=consumidor)


@app.route('/resumo_compra/<int:consumidor_id>')
def resumo_compra(consumidor_id):
    consumidor = Consumidor.query.get_or_404(consumidor_id)
    
    total_poluicao = 0
    produtos_selecionados = []
    
    # Buscar produtos comprados e quantidades
    resultado = db.session.execute(
        consumidor_produto.select().where(consumidor_produto.c.consumidor_id == consumidor.id)
    ).fetchall()

    for row in resultado:
        produto = Produto.query.get(row.produto_id)
        quantidade = row.quantidade
        total_poluicao += produto.custo_poluicao * quantidade
        produtos_selecionados.append((produto, quantidade))

    return render_template('resumo_compra.html', consumidor=consumidor, total_poluicao=total_poluicao, produtos_selecionados=produtos_selecionados)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
