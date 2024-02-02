import sqlite3

class TaskManager:
    def __init__(self,database):
        self.database=database

    def create_table(self):
        con = sqlite3.connect(self.database)
        with con:
            con.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                id_user INTEGER
            )
            """)
            con.commit()
        

    def add_task(self, user_id, name, description):
        con = sqlite3.connect(self.database)
        with con:
            con.execute("INSERT INTO tasks (id_user, name, description) VALUES(?, ?, ?)", (user_id, name, description))
            

    def delete_task(self, task_name: str):
        con = sqlite3.connect(self.database)
        with con:
            con.execute("DELETE FROM tasks WHERE name = ?", (task_name,))
            con.commit()

   

manager = TaskManager("task_history.db")
manager.create_table()
