import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
    CREATE TABLE administradores (
        id SERIAL PRIMARY KEY,
        usuario TEXT UNIQUE NOT NULL,
        hash TEXT NOT NULL
    );
""")