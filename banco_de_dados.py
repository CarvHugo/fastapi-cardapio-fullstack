import sqlite3
    
def garantir_tabela_produtos():
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        descricao TEXT NOT NULL,
        imagem TEXT NOT NULL
    );
    """)
    
    conexao.commit()
    conexao.close()

def buscar_produtos(nome=None, categoria=None, ordenar=None):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    query = "SELECT id, nome, categoria, preco, imagem, descricao FROM produtos"
    
    condicoes = []
    
    parametros = []
    
    if nome:
        condicoes.append("nome LIKE ?")
        parametros.append(f"%{nome}%")
    
    if categoria:
        condicoes.append("categoria LIKE ?")
        parametros.append(f"%{categoria}%")
        
    if condicoes:
        query += " WHERE " + " AND ".join(condicoes)
    
    if ordenar == "nome":
        query += " ORDER BY nome;"
        
    elif ordenar == "categoria":
        query += " ORDER BY categoria;"
        
    elif ordenar == "preco":
        query += " ORDER BY preco;"
        
    cursor.execute(query, parametros)
    
    produtos = cursor.fetchall()
    
    conexao.close()
    
    return produtos

def cadastra_produtos(nome, categoria, preco, imagem=None, descricao=None):
    nome = nome.strip()
    categoria = categoria.strip()
    
    if imagem:
        imagem = imagem.strip()
        
    if descricao:
        descricao = descricao.strip()
    
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    if nome != "" and categoria != "" and preco > 0 and imagem and descricao:
        cursor.execute("INSERT INTO produtos (nome, categoria, preco, imagem, descricao) VALUES (?, ?, ?, ?, ?)", (nome, categoria, preco, imagem, descricao))

        conexao.commit()
        conexao.close()

        return nome, categoria, preco, imagem, descricao
    
    elif nome != "" and categoria != "" and preco > 0 and imagem and not descricao:
        cursor.execute("INSERT INTO produtos (nome, categoria, preco, imagem) VALUES (?, ?, ?, ?)", (nome, categoria, preco, imagem))
        
        conexao.commit()
        conexao.close()
        
        return nome, categoria, preco, imagem
    
    elif nome != "" and categoria != "" and preco > 0 and not imagem and descricao:
            cursor.execute("INSERT INTO produtos (nome, categoria, preco, descricao) VALUES (?, ?, ?, ?)", (nome, categoria, preco, descricao))
            
            conexao.commit()
            conexao.close()
            
            return nome, categoria, preco, descricao
    
    elif nome != "" and categoria != "" and preco > 0 and not imagem and not descricao:
        cursor.execute("INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)", (nome, categoria, preco))
        
        conexao.commit()
        conexao.close()
        
        return nome, categoria, preco
    
    
def tenta_delecao(id):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    verificador_de_linha = cursor.fetchone()

    if verificador_de_linha is not None:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        
        conexao.commit()
        conexao.close()
        return {"message": f'{id} deletado!'}
    
    conexao.close()
    return None


def consulta_produto(id):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome, categoria, preco, imagem, descricao FROM produtos WHERE id = ?;", (id,))
    produto = cursor.fetchone()
    
    if produto:
        nome, categoria, preco, imagem, descricao = produto
        dados = {}
        
        dados['nome'] = nome
        dados['categoria'] = categoria
        dados['preco'] = preco
        dados['imagem'] = imagem
        dados['descricao'] = descricao
        
        return dados
    
    return None

def atualiza_produto(id, nome=None, categoria=None, preco=None, imagem=None, descricao=None):
    conexao = sqlite3.connect("cardapio.db")
    cursor = conexao.cursor()
    
    if not nome or not categoria or not preco:
        conexao.close()
        return None
    
    informacoes_dos_produtos = (nome, categoria, preco, imagem, descricao)
    
    linhas_afetadas = 0
    
    variavel_da_query_sql = ["nome", "categoria", "preco", "imagem", "descricao"]
        
    for contador, dado in enumerate(informacoes_dos_produtos):
        if dado is not None:
            cursor.execute(f"""
                           UPDATE produtos
                           SET {variavel_da_query_sql[contador]} = ?
                           WHERE id = ?
                           """, (dado, id))
            linhas_afetadas += cursor.rowcount

    if linhas_afetadas == 0:
        conexao.close()
        return False
    
    conexao.commit()
    conexao.close()
    
    return True
    
    