import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
    CREATE TABLE produtos (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco NUMERIC(10, 2) NOT NULL,
        descricao TEXT NOT NULL,
        imagem TEXT NOT NULL
    );
""")