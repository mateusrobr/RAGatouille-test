import sqlite3


class IndexDB:
    def __init__(self):
        self.conn = sqlite3.connect('db/index.bd')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS indexes (
        id INTEGER PRIMARY KEY,
        nome TEXT
    )
''')
        
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


    def add_index(self,index_name):
        self.cursor.execute('''
            INSERT INTO cardapio (nome)
            VALUES (?)
        ''', (index_name))
        self.conn.commit()


    def get_index_by_name(self,index_name):
        self.cursor.execute('''
            SELECT * FROM index WHERE nome = ?    
''', (index_name))
        items = self.cursor.fetchall()
        return items
