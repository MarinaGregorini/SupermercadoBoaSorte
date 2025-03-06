# Classes
class Transportadora:
    def __init__(self, nome, emissao_co2):
        self.nome = nome
        self.emissao_co2 = emissao_co2  # Escala de 1 a 5

class Produtor:
    def __init__(self, nome, poluicao_producao):
        self.nome = nome
        self.poluicao_producao = poluicao_producao  # Escala de 1 a 5

class Produto:
    def __init__(self, nome, produtor, transportadora):
        self.nome = nome
        self.produtor = produtor
        self.transportadora = transportadora
        self.custo_poluicao = produtor.poluicao_producao + transportadora.emissao_co2  # Escala de 2 a 10

class Consumidor:
    def __init__(self, nome):
        self.nome = nome
        self.produtos_selecionados = []
    
    def calcular_poluicao_total(self):
        return sum(produto.custo_poluicao for produto in self.produtos_selecionados)
    
# Dados fictícios
transportadoras = [
    Transportadora("EcoTrans", 2),
    Transportadora("FastDelivery", 4)
]

produtores = [
    Produtor("Fazenda Verde", 2),
    Produtor("AgroVida", 3),
    Produtor("EcoFrutas", 4)
]

produtos = [
    Produto("Maçã", produtores[0], transportadoras[0]),
    Produto("Maçã", produtores[1], transportadoras[1]),
    Produto("Maçã", produtores[2], transportadoras[0]),
    Produto("Laranja", produtores[0], transportadoras[1]),
    Produto("Laranja", produtores[1], transportadoras[0]),
    Produto("Laranja", produtores[2], transportadoras[1]),
    Produto("Banana", produtores[0], transportadoras[0]),
    Produto("Banana", produtores[1], transportadoras[1]),
    Produto("Banana", produtores[2], transportadoras[0]),
]

