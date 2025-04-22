import sqlite3


class IndexDB:
    def __init__(self):
        self.conn = sqlite3.connect('db/index.bd')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS indexes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        descricao TEXT
    )
''')
        
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


    def add_index(self,index_name,desc):
        self.cursor.execute('''
            INSERT INTO indexes (nome, descricao)
            VALUES (?,?)
        ''', (index_name,desc))
        self.conn.commit()


    def get_index_by_name(self, index_name):
        self.cursor.execute('''
            SELECT * FROM indexes WHERE nome = ?    
''', (index_name,))
        items = self.cursor.fetchall()
        return items
    
    def is_index_stored(self,index_name):
        result = self.get_index_by_name(index_name=index_name)
        if result:
            return True
        
        return False
    
    def get_all_indexes(self):
        self.cursor.execute("SELECT * FROM indexes")
        results = self.cursor.fetchall()
        return results


