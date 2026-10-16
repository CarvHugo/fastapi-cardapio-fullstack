import sqlite3
from dotenv import load_dotenv
from banco_de_dados import conectar_banco_localmente


load_dotenv()

conexao_sqlite = sqlite3.connect("cardapio.db")

cursor_sqlite = conexao_sqlite.cursor()

cursor_sqlite.execute("""
                SELECT nome, categoria, preco, descricao, imagem
                FROM produtos;
""")

produtos = cursor_sqlite.fetchall()

conexao_postgresql_localhost = conectar_banco_localmente()

cursor_postgresql_localhost = conexao_postgresql_localhost.cursor()

for produto in produtos:
    cursor_postgresql_localhost.execute("""
                                    INSERT 
                                    INTO 
                                    produtos 
                                    (nome, categoria, preco, descricao, imagem) 
                                    VALUES 
                                    (%s, %s, %s, %s, %s)
                                    """, 
                                    (produto[0], produto[1], produto[2], produto[3], produto[4]))

conexao_postgresql_localhost.commit()
conexao_postgresql_localhost.close()

conexao_sqlite.close()
print("Transferência realizada com sucesso!")
