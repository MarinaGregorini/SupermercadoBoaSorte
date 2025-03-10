# Supermercado Boa Sorte

## Descrição
Este é um projeto web desenvolvido com Flask que permite aos utilizadores selecionar produtos com base no seu impacto ambiental. O objetivo é promover escolhas mais sustentáveis ao fazer compras online.

## Funcionalidades
- Login de utilizador
- Escolha de produtos com recomendações
- Cálculo do impacto ambiental dos produtos
- Resumo da compra

## Tecnologias Utilizadas
- Python (Flask)
- HTML, CSS (Bootstrap)

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/MarinaGregorini/SupermercadoBoaSorte
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
- **Variáveis:**
  - `app`: Instância do Flask
  - `consumidor`: Objeto global do utilizador logado
- **Funções:**
  - `login()`: Processa o login do utilizador
  - `escolher_produtos()`: Exibe os produtos e permite selecionar quantidades
  - `resumo_compra()`: Mostra o impacto ambiental total da compra

### classes.py
- **Classes:**
  - `Transportadora`: Representa uma empresa de transporte
  - `Produtor`: Representa um fornecedor de produtos
  - `Produto`: Representa um produto com cálculo do impacto ambiental
  - `Consumidor`: Guarda os produtos escolhidos e calcula o impacto total
- **Variáveis Importantes:**
  - `transportadoras`: Lista de transportadoras disponíveis
  - `produtores`: Lista de produtores de produtos
  - `produtos`: Lista de produtos comercializados

## Autores
Desenvolvido por Bruna Dutra, Marina Gregorini, Marta Santos e Tiago Silva.
