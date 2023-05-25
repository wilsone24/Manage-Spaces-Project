from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash
from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="wilsone",
    password="WmEo.1739",
    database="pagina"
)
cursor = db.cursor()

@app.route('/')
def inicio():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home', nombre= logged_user.fullname))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/register', methods =['GET','POST'])  #GET acceder al formulario, POST enviar datos (crear registros)"""
def register():
    if request.method=='POST':
        username = request.form['username2']
        password = request.form['password2']
        fullname = request.form['fullname2']
        sql = 'INSERT INTO Usuarios (id ,username, password, fullname) VALUES (%s, %s, %s, %s)'
        values = (0,username, generate_password_hash(password), fullname)
        cursor.execute(sql, values)
        db.commit()      
        return redirect(url_for('index'))                        
    return render_template('auth/register.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))


@app.route('/home/<nombre>')
def home(nombre):
    return render_template('home.html', nombre = nombre)

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()