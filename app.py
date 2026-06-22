from flask import Flask, render_template,request,redirect,url_for, session
from database import create_table, save_user, find_user,user_exists
from dotenv import load_dotenv
import os
import bcrypt
import string


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
create_table()


@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/login', methods= ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form['password' ]
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
        password = request.form['password' ]

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
    return render_template('dashboard.html', username= username)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

