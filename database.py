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
    connection.close()
    return cursor.fetchone()




def user_exists(username):
    connection = sqlite3.connect('users.db')
    find_user(username)
    return find_user(username)


