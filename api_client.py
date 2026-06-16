import requests
from requests.exceptions import ConnectionError, RequestException
import os

API_KEY = os.getenv("API_KEY")

HEADERS = {"X-API-KEY": API_KEY}

link_render = "https://fastapi-cardapio-api.onrender.com"
link_testes = "http://127.0.0.1:8000"

def obter_lista_do_cardapio():
    try:
        resposta = requests.get(f"{link_testes}/produtos")

    except ConnectionError:
        return (f'\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')

    except RequestException:
        return(f'\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        produtos = resposta.json()
        
        return produtos
    
    else:    
        return(f'\033[31mOcorreu um erro ao buscar os produtos!\033[m. HTTP {resposta.status_code}')

def cadastrar_produto(nome, categoria, preco):  
    try:
    
        resposta = requests.post(
            link_testes + "/produtos",
            
            json={
                "nome": nome,
                "categoria": categoria,
                "preco": preco
            },
            
            headers=HEADERS
        )
    
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return(f'\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        return (f'\033[32mProduto cadastrado com sucesso no banco de dados! HTTP {resposta.status_code}\033[m')
    
    else:
        return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')


def deletar_produto(id: int):
    try:
        resposta = requests.delete(f'{link_testes}/produtos/{id}',
        headers=HEADERS
        )
        
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return ('\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        return (f'\033[32mProduto deletado com sucesso! HTTP {resposta.status_code}\033[m')
    
    else:
        if resposta.status_code == 404:
            detalhe_da_resposta = resposta.json()['detail']
            return f'\033[31m{detalhe_da_resposta}\033[m'
        
        return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')
    
def atualizar_produto(id=None, nome=None, categoria=None, preco=None):
    dados = {}
    
    if nome is not None:
        dados['nome'] = nome
        
    if categoria is not None:
        dados['categoria'] = categoria
        
    if preco is not None:
        dados['preco'] = preco 
    
    try:
        resposta = requests.patch(
        f'{link_testes}/produtos/{id}', json=dados, headers=HEADERS)   
    
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return ('\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200,300):
        return (f"\033[32mProduto atualizado com sucesso! HTTP {resposta.status_code}\033[m")
    
    elif resposta.status_code in (404, 422):
        detalhe_da_resposta = resposta.json()['detail']
        return (f'\033[31m{detalhe_da_resposta}\033[m')
    
    return (f'\033[31mOcorreu um erro. Tente novamente! HTTP {resposta.status_code}\033[m')

def consultar_produto(id):
    try:
        resposta = requests.get(f'{link_testes}/produtos/{id}')
        
    except ConnectionError:
        return ('\033[31mNão foi possível conectar à API. Verifique se o servidor está rodando.\033[m')
    
    except RequestException:
        return ('\033[31mOcorreu um erro! Tente novamente\033[m')
    
    if resposta.status_code in range(200, 300):
        produto = resposta.json()
        
        return produto
    
    elif resposta.status_code == 404:
        resposta = resposta.json()
        resposta = resposta['detail']
        
        return (f'\033[31m{resposta}\033[m')