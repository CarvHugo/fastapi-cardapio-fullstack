# FastAPI Cardápio Fullstack

[![Frontend Online](https://img.shields.io/badge/Frontend-Online-success?style=for-the-badge)](https://site-cardapio-iqmd.onrender.com)
[![API Docs](https://img.shields.io/badge/API-Docs-blue?style=for-the-badge)](https://fastapi-cardapio-api.onrender.com/docs)

Projeto fullstack de gerenciamento de cardápio desenvolvido com Python, FastAPI, SQLite, HTML e CSS.

A aplicação evoluiu de um projeto de estudos para uma arquitetura composta por três camadas integradas:

* Frontend Web para apresentação do restaurante;
* API REST para gerenciamento de produtos;
* CLI administrativa para consumo e gerenciamento da API.

O projeto foi desenvolvido com o objetivo de aplicar conceitos práticos de desenvolvimento fullstack, integração cliente-servidor, persistência de dados, autenticação, deploy e organização de código.

---

# Demonstração

## Frontend Web

Acesse a aplicação online:

https://site-cardapio-iqmd.onrender.com

## API REST

Documentação interativa da API:

https://fastapi-cardapio-api.onrender.com/docs


> **Observação:** A API está hospedada no plano gratuito do Render e pode levar alguns segundos para inicializar após períodos de inatividade. Caso o cardápio não carregue imediatamente, aguarde alguns instantes e recarregue a página.
---

# Tecnologias Utilizadas

## Frontend

* HTML5
* CSS3

## Backend

* Python
* FastAPI
* SQLite3
* Requests
* Uvicorn

## Infraestrutura

* Render
* Git
* GitHub

---

# Funcionalidades

## Frontend Web

* Página inicial do restaurante;
* Página de cardápio;
* Página institucional;
* Navegação entre páginas;
* Hospedagem online via Render.

## API REST

* Cadastro de produtos;
* Listagem de produtos;
* Consulta de produto por ID;
* Atualização parcial de produtos (PATCH);
* Exclusão de produtos.

## Segurança

* Autenticação via API Key em endpoints protegidos.

## CLI Administrativa

* Cadastro de produtos;
* Consulta de produtos;
* Atualização de produtos;
* Exclusão de produtos;
* Consumo de endpoints HTTP utilizando Requests.

---

# Estrutura do Projeto

```text
fastapi-cardapio-api/
│
├── app.py
├── api_client.py
├── banco_de_dados.py
├── cli.py
├── funcoes_da_cli.py
├── operador_do_cli.py
├── requirements.txt
├── cardapio.db
│
├── frontend/
│   ├── css/
│   ├── imagens/
│   ├── index.html
│   ├── cardapio.html
│   └── historia.html
│
└── README.md
```

---

# Como Executar a CLI

**Obs:** A API encontra-se hospedada online no Render. Não é necessário executar o servidor FastAPI localmente para utilizar a CLI.

### 1. Clone o repositório

```bash
git clone https://github.com/CarvHugo/fastapi-cardapio-api
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a variável de ambiente da API Key

PowerShell:

```powershell
$env:API_KEY="nidhogg2026"
```

### 4. Execute a CLI

```bash
python cli.py
```

---

# Objetivos de Aprendizado

* Desenvolvimento de APIs REST com FastAPI;
* Operações CRUD;
* Banco de dados relacionais;
* Integração cliente-servidor;
* Autenticação via API Key;
* Refatoração e organização de código;
* Deploy de aplicações;
* Desenvolvimento Fullstack.
