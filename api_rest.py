from flask import Flask, request, jsonify
from models import *
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_supermercado.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# --------------------------
# Rotas básicas
# --------------------------

# Listar consumidores
@app.route('/api/consumidores/', methods=['GET'])
def get_consumidores():
    consumidores = Consumidor.query.all()
    return jsonify([{'id': c.id, 'nome': c.nome} for c in consumidores])

# Criar consumidor
@app.route('/api/consumidores/', methods=['POST'])
def create_consumidor():
    data = request.get_json()
    consumidor = Consumidor(nome=data.get('nome'))
    db.session.add(consumidor)
    db.session.commit()
    return jsonify({'id': consumidor.id, 'nome': consumidor.nome}), 201

# Listar transportadoras
@app.route('/api/transportadoras/', methods=['GET'])
def get_transportadoras():
    transportadoras = Transportadora.query.all()
    return jsonify([{
        'id': t.id, 
        'nome': t.nome, 
        'co2_km': t.co2_km, 
        'eletrica': t.eletrica
    } for t in transportadoras])

# Listar produtores
@app.route('/api/produtores/', methods=['GET'])
def get_produtores():
    produtores = Produtor.query.all()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'consumo_produto': p.consumo_produto,
        'consumo_diario': p.consumo_diario,
        'distancia_km': p.distancia_km,
        'dias_armazenado': p.dias_armazenado
    } for p in produtores])

# Listar produtos
@app.route('/api/produtos/', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'produtor_id': p.produtor_id,
        'transportadora_id': p.transportadora_id,
        'custo_poluicao': p.custo_poluicao
    } for p in produtos])

# Consumidor escolhe produtos
@app.route('/api/consumidores/<int:consumidor_id>/produtos/', methods=['POST'])
def escolher_produtos(consumidor_id):
    consumidor = Consumidor.query.get_or_404(consumidor_id)
    data = request.get_json()

    db.session.execute(consumidor_produto.delete().where(consumidor_produto.c.consumidor_id == consumidor.id))

    for item in data.get('produtos', []):
        produto_id = item.get('produto_id')
        quantidade = item.get('quantidade', 0)
        if quantidade > 0:
            db.session.execute(consumidor_produto.insert().values(
                consumidor_id=consumidor.id,
                produto_id=produto_id,
                quantidade=quantidade
            ))

    db.session.commit()
    return jsonify({'message': 'Produtos escolhidos com sucesso'}), 201

# Resumo da compra
@app.route('/api/consumidores/<int:consumidor_id>/resumo/', methods=['GET'])
def resumo_compra(consumidor_id):
    consumidor = Consumidor.query.get_or_404(consumidor_id)
    total_poluicao = 0
    produtos_selecionados = []

    resultado = db.session.execute(
        consumidor_produto.select().where(consumidor_produto.c.consumidor_id == consumidor.id)
    ).fetchall()

    for row in resultado:
        produto = Produto.query.get(row.produto_id)
        quantidade = row.quantidade
        total_poluicao += produto.custo_poluicao * quantidade
        produtos_selecionados.append({
            'produto': {
                'id': produto.id,
                'nome': produto.nome,
                'produtor_id': produto.produtor_id,
                'transportadora_id': produto.transportadora_id,
                'custo_poluicao': produto.custo_poluicao
            },
            'quantidade': quantidade
        })

    return jsonify({
        'consumidor': {'id': consumidor.id, 'nome': consumidor.nome},
        'total_poluicao': total_poluicao,
        'produtos_selecionados': produtos_selecionados
    })

# --------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
