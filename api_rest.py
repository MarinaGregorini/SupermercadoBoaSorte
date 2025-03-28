from flask import Flask, request
from models import *
from flask_restful import fields, marshal_with, Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_supermercado.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

api = Api(app)

# --------------------------
# Serializers
# --------------------------

transportadora_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'co2_km': fields.Float,
    'eletrica': fields.Boolean
}

produtor_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'consumo_produto': fields.Float,
    'consumo_diario': fields.Float,
    'distancia_km': fields.Float,
    'dias_armazenado': fields.Integer
}

produto_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'produtor_id': fields.Integer,
    'transportadora_id': fields.Integer,
    'custo_poluicao': fields.Integer
}

consumidor_fields = {
    'id': fields.Integer,
    'nome': fields.String
}

produto_com_quantidade_fields = {
    'produto': fields.Nested(produto_fields),
    'quantidade': fields.Integer
}

resumo_fields = {
    'consumidor': fields.Nested(consumidor_fields),
    'total_poluicao': fields.Integer,
    'produtos_selecionados': fields.List(fields.Nested(produto_com_quantidade_fields))
}

# --------------------------
# Recursos REST
# --------------------------

class Consumidores(Resource):
    @marshal_with(consumidor_fields)
    def get(self):
        return Consumidor.query.all()

    @marshal_with(consumidor_fields)
    def post(self):
        args = user_args.parse_args()
        consumidor = Consumidor(nome=args['nome'])
        db.session.add(consumidor)
        db.session.commit()
        return consumidor, 201


class Transportadoras(Resource):
    @marshal_with(transportadora_fields)
    def get(self):
        return Transportadora.query.all()


class Produtores(Resource):
    @marshal_with(produtor_fields)
    def get(self):
        return Produtor.query.all()


class Produtos(Resource):
    @marshal_with(produto_fields)
    def get(self):
        return Produto.query.all()


class EscolherProdutos(Resource):
    def post(self, consumidor_id):
        consumidor = Consumidor.query.get_or_404(consumidor_id)
        data = request.get_json()

        # Limpa produtos antigos
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
        return {'message': 'Produtos escolhidos com sucesso'}, 201


class ResumoCompra(Resource):
    @marshal_with(resumo_fields)
    def get(self, consumidor_id):
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
                'produto': produto,
                'quantidade': quantidade
            })

        return {
            'consumidor': consumidor,
            'total_poluicao': total_poluicao,
            'produtos_selecionados': produtos_selecionados
        }

# --------------------------
# Registro das rotas
# --------------------------

api.add_resource(Consumidores, '/api/consumidores/')
api.add_resource(Transportadoras, '/api/transportadoras/')
api.add_resource(Produtores, '/api/produtores/')
api.add_resource(Produtos, '/api/produtos/')
api.add_resource(EscolherProdutos, '/api/consumidores/<int:consumidor_id>/produtos/')
api.add_resource(ResumoCompra, '/api/consumidores/<int:consumidor_id>/resumo/')

# --------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
