import sqlite3

class ScheduleModel:
    def __init__(self, db_name='app.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def add_schedule(self, title, date, time, description):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO schedules (title, date, time, description) VALUES (?, ?, ?, ?)',
                       (title, date, time, description))
        self.conn.commit()

    def get_schedules(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM schedules')
        return cursor.fetchall()