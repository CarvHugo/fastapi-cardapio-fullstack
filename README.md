# FastAPI Cardápio Fullstack

[![Frontend Online](https://img.shields.io/badge/Frontend-Online-success?style=for-the-badge)](https://site-cardapio-iqmd.onrender.com)

[![API Docs](https://img.shields.io/badge/API-Docs-blue?style=for-the-badge)](https://fastapi-cardapio-api.onrender.com/docs)

Projeto fullstack de gerenciamento de cardápio desenvolvido com Python, FastAPI, PostgreSQL, HTML, CSS e JavaScript.

A aplicação evoluiu de um projeto de estudos baseado em SQLite para uma arquitetura web composta por três camadas integradas:

* **Frontend Web** para apresentação do restaurante e interação com o cardápio;
* **API REST** desenvolvida com FastAPI para gerenciamento dos produtos;
* **Banco de dados PostgreSQL** hospedado no Supabase para persistência dos dados.

## Objetivos e Evolução

O projeto foi desenvolvido inicialmente com o objetivo de aplicar conceitos práticos de desenvolvimento fullstack, integração cliente-servidor, APIs REST, operações CRUD, persistência de dados, autenticação, variáveis de ambiente, migração de banco de dados, deploy e organização de código.

No entanto, o **Cucina di Milano não foi pensado apenas como um projeto de estudo**. A proposta é continuar evoluindo a aplicação até que ela possa se tornar de uma solução real para gerenciamento e apresentação de um cardápio digital.

Entre os próximos objetivos estão a evolução da experiência do usuário, aprimoramento da segurança, expansão das funcionalidades administrativas, melhoria da arquitetura e adoção de práticas utilizadas em aplicações reais.

Dessa forma, o projeto funciona tanto como um ambiente contínuo de aprendizado quanto como uma aplicação em desenvolvimento, permitindo que novas tecnologias e conceitos sejam incorporados conforme suas necessidades evoluem.


---

# Demonstração

## Frontend Web

Acesse a aplicação online:

https://site-cardapio-iqmd.onrender.com

## API REST

Documentação interativa da API:

https://fastapi-cardapio-api.onrender.com/docs

---

# Tecnologias Utilizadas

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* FastAPI
* Pydantic
* psycopg
* Uvicorn

## Banco de Dados

* PostgreSQL
* Supabase

## Infraestrutura e Ferramentas

* Render
* Git
* GitHub
* python-dotenv

---

# Funcionalidades

## Frontend Web

* Página inicial do restaurante;
* Página de cardápio;
* Página institucional;
* Navegação entre páginas;
* Busca de produtos;
* Filtragem por categoria;
* Ordenação de produtos;
* Integração com a API REST;
* Hospedagem online via Render.

## API REST

* Cadastro de produtos;
* Listagem de produtos;
* Consulta de produto por ID;
* Busca de produtos por nome;
* Filtragem por categoria;
* Ordenação por nome, categoria ou preço;
* Atualização parcial de produtos utilizando PATCH;
* Exclusão de produtos.

## Banco de Dados

* Persistência dos produtos utilizando PostgreSQL;
* Criação automática da tabela de produtos caso ela não exista;
* Conexão utilizando `DATABASE_URL`;
* Migração dos dados originalmente armazenados em SQLite para PostgreSQL.

## Segurança

* Autenticação via API Key nos endpoints de cadastro, atualização e exclusão;
* Credenciais armazenadas por meio de variáveis de ambiente;
* Separação entre configurações locais e de produção.

---

# Migração do Banco de Dados

O projeto originalmente utilizava SQLite como banco de dados local.

Com a evolução da aplicação, o banco foi migrado para PostgreSQL hospedado no Supabase.

O processo de migração envolveu:

1. Criação da estrutura equivalente em PostgreSQL;
2. Configuração de uma conexão PostgreSQL local para testes;
3. Migração dos dados existentes do SQLite para PostgreSQL;
4. Criação do banco PostgreSQL no Supabase;
5. Transferência dos dados para o banco em nuvem;
6. Adaptação da camada de acesso ao banco para utilizar PostgreSQL;
7. Testes da API utilizando o banco hospedado no Supabase.

A aplicação utiliza `DATABASE_URL` para estabelecer a conexão com o banco em produção.

---

# Estrutura do Projeto

```text
cardapio-fullstack/

│
├── frontend/
│    ├── admin.html
│    ├── cardapio.html
│    ├── index.html
│    ├── css/
│    └── imagens/
│        ├── produtos/
│        ├── ui/
│        └── videos/
│
├── legacy/
│   ├── api_client.py
│   ├── cli.py
│   ├── funcoes_da_cli.py
│   └── operador_do_cli.py
│
├── scripts/
│   ├── cria_tabela_na_nuvem.py
│   ├── migracao_sqlite_postgresql.py
│   └── transfere_tabela_para_nuvem.py
│
├── app.py
├── banco_de_dados.py
├── requirements.txt
├── .gitignore
├── .gitattributes
│
└── README.md
```

> A pasta `legacy/` contém código relacionado à antiga interface CLI do projeto. Essa camada foi aposentada após a evolução da aplicação para uma arquitetura web.

---

# Configuração

Para executar o projeto localmente, é necessário configurar as variáveis de ambiente utilizadas pela aplicação.

Exemplo:

```env
DATABASE_URL=postgresql://...
API_KEY=...
```

---

# Objetivos de Aprendizado

* Desenvolvimento de APIs REST com FastAPI;
* Desenvolvimento Fullstack;
* Operações CRUD;
* Banco de dados relacionais;
* PostgreSQL;
* Integração cliente-servidor;
* Autenticação via API Key;
* Variáveis de ambiente;
* Migração de SQLite para PostgreSQL;
* Integração com banco de dados em nuvem;
* Refatoração e organização de código;
* Deploy de aplicações;
* Versionamento com Git e GitHub.
