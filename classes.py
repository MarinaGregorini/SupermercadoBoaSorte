# Classes
class Transportadora:
    def __init__(self, nome, co2_km, eletrica=False):
        self.nome = nome
        self.co2_km = co2_km  
        self.eletrica = eletrica  

class Produtor:
    def __init__(self, nome, consumo_produto, consumo_diario, distancia_km, dias_armazenado):
        self.nome = nome
        self.consumo_produto = consumo_produto
        self.consumo_diario = consumo_diario
        self.distancia_km = distancia_km
        self.dias_armazenado = dias_armazenado
class Produto:
    def __init__(self, nome, produtor, transportadora):
        self.nome = nome
        self.produtor = produtor
        self.transportadora = transportadora
        
        self.poluicao_producao = self.calcular_poluicao_producao()
        self.poluicao_transporte = self.calcular_poluicao_transporte()
        self.custo_poluicao = self.poluicao_producao + self.poluicao_transporte
        
    def calcular_poluicao_producao(self):
        
        poluicao_producao = self.produtor.consumo_produto + (self.produtor.dias_armazenado * self.produtor.consumo_diario)
        if poluicao_producao <= 2:
            poluicao_producao_rank = 1
        elif poluicao_producao > 2:
            poluicao_producao_rank = 2
        else:
            poluicao_producao_rank = 3
            
        return poluicao_producao_rank
    
    def calcular_poluicao_transporte(self):
        
        poluicao_transporte = 0 if self.transportadora.eletrica else self.produtor.distancia_km * self.transportadora.co2_km
        if poluicao_transporte < 52000:
            poluicao_transporte_rank = 1
        elif poluicao_transporte > 52000 and poluicao_transporte < 74000:
            poluicao_transporte_rank = 2
        else:
            poluicao_transporte_rank = 3
            
        return  poluicao_transporte_rank
        

class Consumidor:
    def __init__(self, nome):
        self.nome = nome
        self.produtos_selecionados = []
    
    def calcular_poluicao_total(self):
        return sum(produto.custo_poluicao for produto in self.produtos_selecionados)


transportadoras = [
    Transportadora("EcoTrans", 0, eletrica=True), 
    Transportadora("FastDelivery", 738)  
]

produtores = [
    Produtor("Fazenda Verde", 2.1, 0.2, 100, 3),
    Produtor("AgroVida", 1.5, 0.2, 70, 4),
    Produtor("EcoFrutas", 1.8, 0.1, 150, 2)
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