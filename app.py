from flask import Flask, render_template,request,redirect,url_for, session
from database import create_table, save_user, find_user,user_exists
from dotenv import load_dotenv
import os
import bcrypt


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
        passwordL = request.form['password' ]
    # Check User input Exist 
        if user_exists(username):
            if bcrypt.checkpw(passwordL.encode('utf-8'), find_user(username)[1]):
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                return render_template('Login.html',error = 'Wrong Password')
        else :
            return render_template('Login.html', error='User not found')

    return render_template('Login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)