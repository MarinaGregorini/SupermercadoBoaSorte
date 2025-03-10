# Supermercado Boa Sorte

## Descrição
Este é um projeto web desenvolvido com Flask que permite aos utilizadores selecionar produtos com base no seu impacto ambiental. O objetivo é promover escolhas mais sustentáveis ao fazer compras online.

## Funcionalidades
- Identificação do utilizador
- Escolha de produtos com recomendações dos que causam menor impacto ambiental
- Cálculo do impacto ambiental dos produtos
- Resumo dos produtos selecionados

## Tecnologias Utilizadas
- Python (Flask)
- HTML, CSS (Bootstrap)

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/MarinaGregorini/SupermercadoBoaSorte.git
cd SupermercadoBoaSorte
```

### 2. Criar um Ambiente Virtual e Instalar Dependências
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Executar a Aplicação
```bash
python app.py
```

### 4. Aceder à Web App
Depois de iniciar a aplicação, abra o navegador e aceda a:
```
http://127.0.0.1:5000/
```

## Estrutura do Projeto
```
/
├── static/
│   ├── styles.css
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── escolher_produtos.html
│   ├── resumo_compra.html
├── app.py
├── classes.py
├── requirements.txt
├── README.md
```

## Variáveis e Funções

### app.py
- **Funções:**
  - `login()`: Identifica o utilizador e instancia a classe consumidor
  - `escolher_produtos()`: Lista os produtos, define o produto que tem o menor impacto ambiental, recebe a seleção do cliente e a quantidade de produtos selecionados
  - `resumo_compra()`: Calcula o total da poluição gerada pelos produtos selecionados pelo cliente

### classes.py
- **Classes:**
  - `Transportadora`: Define as empresas de transporte.
    - Recebe os seguintes parâmetros:
      - `nome`
      - `co2_km` representa a emissão de co2 por km do veículo
      - `eletrica` define se o veículo é elétrico

  - `Produtor`: Representa os fornecedores de produtos.
    - Recebe os seguintes parâmetros:
      - `nome`
      - `consumo_produto` define quantos kWh são gastos para produzir cada produto
      - `consumo_diario` define os gastos em kWh que o produtor gasta por dia para manter os seus produtos armazenados
      - `distancia_km` define a distância entre o produtor e o supermercado 
      - `dias_armazenado` define quantos dias o produtor mantem os seus produtos armazenados antes de os enviar

  - `Produto`: Representa um produto.
    - Recebe os seguintes parâmetros:
      - `nome`
      - `produtor`
      - `transportadora`
  
  O método `calcular_poluicao_producao()` calcula o impacto ambiental da produção através do somatório dos gastos energéticos do consumo diário do armazenamento, multiplicados pelos dias armazenados, com o gasto energético da produção do produto. 
  Esta dimensão do impacto ambiental é então colocado num ranking que vai de 1 a 3, de acordo com o total de kWh.

  O método `calcular_poluicao_transporte()` multiplica a distância em km pela emissão de co2 por km. 
  Esta dimensão do impacto ambiental é também colocado num ranking, de 0 a 3, onde os veículos elétricos, que não emitem co2, são equivalentes a 0. Os restantes são dividos de acordo com o total de emissões de CO2.

  - `Consumidor`: Define o consumidor.
    - Recebe o parâmetro `nome`.
      
 Inicializa e popula o dicionário `produtos_selecionados` com a função `adicionar_produto(produto, quantidade)`.
 Calcula o impacto ambiental total relacionado a cada consumidor com a função `calcular_poluicao_total()` que retorna a soma de todos os produtos do dicionário `produtos_selecionados` multiplicados pelas suas quantidades. 

- **Variáveis Importantes:**
  - `transportadoras`: Lista de transportadoras disponíveis
  - `produtores`: Lista de produtores de produtos
  - `produtos`: Lista de produtos comercializados

## Autores
Desenvolvido por Bruna Dutra, Marina Gregorini, Marta Santos e Tiago Silva.
