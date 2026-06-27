import sqlite3



def create_table():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    connection.commit()
    connection.close()




def save_user(username,password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (?,?)",(username, password))
    connection.commit()
    connection.close()




def find_user(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    connection.close()
    return result




def user_exists(username):
    return find_user(username)


def create_tasks_table():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id  INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, task TEXT, done INTEGER DEFAULT 0)")
    connection.commit()
    connection.close()

def add_task(username, task):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (username, task) VALUES (?, ?)", (username, task))
    connection.commit()
    connection.close()

def get_tasks(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE username = ?", (username,))
    result = cursor.fetchall()
    connection.close()
    return result

def delete_task(task_id):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    connection.commit()
    connection.close()

def complete_task(task_id):
    connection =sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?",(task_id,))
    connection.commit()
    connection.close()
