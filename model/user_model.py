import sqlite3

class UserModel:
    def __init__(self, db_name='app.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, name, email, password):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                       (name, email, password))
        self.conn.commit()

    def get_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
