from flask import Flask, render_template,request,redirect,url_for, session
from database import create_table, save_user, find_user,user_exists, create_tasks_table, add_task, get_tasks, delete_task, complete_task , delete_user_tasks, delete_user
from dotenv import load_dotenv
import os
import bcrypt
import string


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
create_table()
create_tasks_table()


@app.route('/')
def home():
    return render_template('Login.html') # Directly to home which is login page

@app.route('/login', methods= ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form['password' ]

        print(find_user(username))
    # Check User input Exist 
        if user_exists(username):
            stored_hash = find_user(username)[1]
            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                return render_template('Login.html',error = 'Wrong Password')
        else :
            return render_template('Login.html', error='User not found')

    return render_template('Login.html')

@app.route('/register', methods= ['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        print(request.form)

        if user_exists(username):
            return render_template('Signup.html' , error='username Already existed')
        elif len(password) < 6:
            return render_template('Signup.html', error='Too Weak')
        elif not any(char.isupper() for char in password):
            return render_template('Signup.html', error='Needs a Capital Letter')
        elif not any(char.isdigit() for char in password):
            return render_template('Signup.html', error='Needs a Number')
        elif not any(char in string.punctuation for char in password):
            return render_template('Signup.html', error='Needs a symbol')
        else:
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            save_user(username,password_hash)
            return redirect(url_for('login'))
    
    return render_template('Signup.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    tasks = get_tasks(username)
    total_tasks = len(tasks)
    completed = len([task for task in tasks if task[3] == 1])   
    if total_tasks > 0:
        percentage = (completed / total_tasks) * 100
    else:
        percentage = 0
    return render_template('dashboard.html', username = username, tasks = tasks, total_tasks=total_tasks,
    completed=completed,
    percentage=percentage)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/add_task' , methods=['POST'])
def add_task_route():
    if 'username' in session:
        username = session['username']
        task = request.form['task']
        add_task(username, task)
        return redirect(url_for('dashboard'))
    
@app.route('/delete_task', methods = ['POST'])
def delete_task_route():
    task = request.form['task_id']
    delete_task(task)
    return redirect(url_for('dashboard'))

@app.route('/complete_task', methods = ['POST'])
def complete_task_route():
    task_id = request.form['task_id']
    complete_task(task_id)
    return redirect(url_for('dashboard'))

@app.route('/delete_account', methods = ['POST'])
def delete_account_route():
    if 'username' in session:
        username = session['username']
        delete_user_tasks(username)
        delete_user(username)
        session.clear()
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

