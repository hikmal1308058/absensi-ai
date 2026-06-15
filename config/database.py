# config/database.py — PostgreSQL untuk Render
import psycopg2
import psycopg2.extras
import os

def get_db():
    conn = psycopg2.connect(
        os.getenv('DATABASE_URL'),  # Render set ini otomatis
        sslmode='require'
    )
    return conn
