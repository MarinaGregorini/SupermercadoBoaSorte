# Classes
class Transportadora:
    def __init__(self, nome, emissao_co2_por_km, eletrica=False, perda_produtos=0):
        self.nome = nome
        self.emissao_co2_por_km = emissao_co2_por_km  
        self.eletrica = eletrica  
        self.perda_produtos = perda_produtos 

class Produtor:
    def __init__(self, nome, consumo_kwh_por_10_produtos, consumo_diario_kwh, distancia_km):
        self.nome = nome
        self.consumo_kwh_por_10_produtos = consumo_kwh_por_10_produtos
        self.consumo_diario_kwh = consumo_diario_kwh
        self.distancia_km = distancia_km

    def calcular_recursos_producao(self, quantidade):
        kwh_producao = (quantidade / 10) * self.consumo_kwh_por_10_produtos
        return kwh_producao + self.consumo_diario_kwh

class Produto:
    def __init__(self, nome, produtor, transportadora, quantidade=10):
        self.nome = nome
        self.produtor = produtor
        self.transportadora = transportadora
        self.quantidade = quantidade
        
        self.custo_poluicao = self.calcular_poluicao()

    def calcular_poluicao(self):
        poluicao_producao = self.produtor.calcular_recursos_producao(self.quantidade)
        poluicao_transporte = 0 if self.transportadora.eletrica else self.produtor.distancia_km * self.transportadora.emissao_co2_por_km
        return poluicao_producao + poluicao_transporte

    def calcular_perda_transporte(self):
        return self.quantidade * self.transportadora.perda_produtos

class Consumidor:
    def __init__(self, nome):
        self.nome = nome
        self.produtos_selecionados = []
    
    def calcular_poluicao_total(self):
        return sum(produto.custo_poluicao for produto in self.produtos_selecionados)


transportadoras = [
    Transportadora("EcoTrans", 0, eletrica=True, perda_produtos=0.2), 
    Transportadora("FastDelivery", 738, eletrica=False)  
]

produtores = [
    Produtor("Fazenda Verde", 1, 2, 100),
    Produtor("AgroVida", 3, 2, 70),
    Produtor("EcoFrutas", 2, 1, 150)
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