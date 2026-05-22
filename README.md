# FastAPI Cardápio Fullstack

Projeto de gerenciamento de cardápio desenvolvido com Python e FastAPI.

A aplicação começou como um projeto de estudos voltado para desenvolvimento web e evoluiu para uma estrutura fullstack integrada, contendo:

- API REST com FastAPI;
- CLI para interação com o sistema;
- Banco de dados SQLite;
- Deploy online;
- Autenticação básica via API Key;
- Operações completas de CRUD.

O objetivo do projeto é aplicar conceitos reais de desenvolvimento backend, organização de código, integração entre sistemas e arquitetura de APIs.

---

# Tecnologias utilizadas

- Python
- FastAPI
- SQLite3
- Requests
- Uvicorn
- Render

---

# Funcionalidades

## API REST
- Cadastro de produtos;
- Listagem de produtos;
- Busca de produto por ID;
- Atualização parcial de produtos (PATCH);
- Deleção de produtos;

## Segurança
- Autenticação via API Key em endpoints protegidos;

## CLI
- Integração da aplicação de terminal com a API;
- Consumo de endpoints HTTP utilizando Requests;

---

# Estrutura do projeto

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
├── css/
├── imagens/
│
├── index.html
├── cardapio.html
├── historia.html
│
└── README.md
```

---

# Como executar a cli

**Obs**: API já está hospedada online no Render, portanto não é necessário executar o servidor FastAPI localmente para utilizar a CLI.

### 1. Clone o repositório

```bash
git clone https://github.com/CarvHugo/fastapi-cardapio-api
```

### 2. Instale as dependências
### No powershell
```bash
pip install -r requirements.txt
```

### 3. Configure a chave de API para realizar CRUD
### No powershell
```bash
$env:API_KEY="nidhogg2026"
```

### 4. Execute a CLI
```bash
python cli.py
```