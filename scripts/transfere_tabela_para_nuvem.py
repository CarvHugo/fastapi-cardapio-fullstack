import psycopg
from dotenv import load_dotenv
import os
from banco_de_dados import conectar_banco

load_dotenv()

conexao_postgre_localhost = conectar_banco()

cursor_postgre_localhost = conexao_postgre_localhost.cursor()

cursor_postgre_localhost.execute("""
                    SELECT 
                    nome, categoria, preco, descricao, imagem 
                    FROM 
                    produtos;
                    """)

produtos = cursor_postgre_localhost.fetchall()


database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as conexao_postgre_nuvem:
    with conexao_postgre_nuvem.cursor() as cursor_postgre_nuvem:
        for produto in produtos:
            cursor_postgre_nuvem.execute("INSERT INTO produtos (nome, categoria, preco, descricao, imagem) VALUES (%s, %s, %s, %s, %s)", (produto[0], produto[1], produto[2], produto[3], produto[4]))
    
conexao_postgre_localhost.close()

print("A transferência de informações entre o banco de dados local e a nuvem foi feita com sucesso!")