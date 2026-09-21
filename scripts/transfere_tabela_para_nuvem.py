import psycopg
from dotenv import load_dotenv
import os
from banco_de_dados import conectar_banco_localmente

load_dotenv()

conexao_postgresql_localhost = conectar_banco_localmente()

cursor_postgresql_localhost = conexao_postgresql_localhost.cursor()

cursor_postgresql_localhost.execute("""
                                SELECT 
                                nome, categoria, preco, descricao, imagem 
                                FROM 
                                produtos;
                                """)

produtos = cursor_postgresql_localhost.fetchall()


database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as conexao_postgresql_nuvem:
    with conexao_postgresql_nuvem.cursor() as cursor_postgresql_nuvem:
        for produto in produtos:
            cursor_postgresql_nuvem.execute("""INSERT 
                                         INTO 
                                         produtos 
                                         (nome, categoria, preco, descricao, imagem) 
                                         VALUES 
                                         (%s, %s, %s, %s, %s)""", 
                                         (produto[0], produto[1], produto[2], produto[3], produto[4]))
    
conexao_postgresql_localhost.close()

print("A transferência de informações entre o banco de dados local e a nuvem foi feita com sucesso!")