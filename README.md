# Flask Site de Compras Sustentáveis

Este projeto é um site desenvolvido com Flask que permite selecionar produtos, produtores e transportadoras, calculando o impacto ambiental de cada compra.

## Estrutura do Projeto

```
/ (Raiz do projeto)
│-- app.py            # Código principal do Flask
│-- classes.py        # Definição das classes do sistema
│-- templates/
│   │-- login.html    # Página de login
│   │-- produtos.html # Página de escolha de produtos
│   │-- resumo.html   # Página de resumo da compra
│-- static/           # Arquivos estáticos (CSS, JS, imagens)
│-- requirements.txt  # Dependências do projeto
│-- README.md         # Este arquivo
```

## Classes (classes.py)

- **Consumidor**
  - Atributos: `nome`, `produtos_selecionados`
  - Métodos: `calcular_valor_total()`
- **Transportadora**
  - Atributos: `nome`, `emissao`
- **Produtor**
  - Atributos: `nome`, `custo_pol`
- **Produto**
  - Atributos: `nome`, `custo_pol_total`
  - Método: `calcular_custo_pol(produtor, transporte)`

## Arquivo Principal (app.py)

### Variáveis
- `transportadoras` → Lista de transportadoras
- `produtores` → Lista de produtores
- `produtos` → Lista de produtos
- `carrinho` → Lista de compras feitas pelo usuário

### Rotas
- `/` → Página de login
- `/produtos` → Página para escolha de produtos
- `/resumo` → Página com o resumo da compra

## Dependências (requirements.txt)

O projeto requer a instalação das seguintes bibliotecas:

```
Flask
```

Instale com:
```sh
pip install -r requirements.txt
```

## Como Executar

1. Criar ambiente virtual (opcional, mas recomendado):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # No macOS/Linux
   venv\Scripts\activate  # No Windows
   ```
2. Instalar dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Rodar a aplicação:
   ```sh
   python app.py
   ```
4. Acessar no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

