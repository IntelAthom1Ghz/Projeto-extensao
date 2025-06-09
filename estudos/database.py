import sqlite3
import os
def init_db():
    os.makedirs('app', exist_ok=True)
    with sqlite3.connect('app/usuarios.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''  CREATE TABLE IF NOT EXISTS usuarios(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEX UNIQUE NOT NULL,
                       senha TEXT NOT NULL
                       ) 
                       ''')
        conn.commit()