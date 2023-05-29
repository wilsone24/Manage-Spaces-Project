#Librerias
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from config import config
from correos import mensajes, Registro_Diario, generarIMG
from models.ModelUser import ModelUser
from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__) 

@app.route('/')
def inicio():
    """Ruta inicial de la aplicación
    """
    return redirect(url_for('index'))

@app.route('/index')
def index():
    """Ruta principal de la pagina web
    """
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Ruta login, para acceder a los distintos servicios, acceder al formulario y enviar datos
    """
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(user)
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
    """Ruta para registrar un usuario, acceder al formulario y enviar datos
    """
    if request.method=='POST':
        username = request.form['username2']
        password = request.form['password2']
        fullname = request.form['fullname2']
        values = (username, generate_password_hash(password), fullname)
        if ModelUser.register(values):
            return redirect(url_for('index'))                        
    return render_template('auth/register.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Ruta Para enviar un mensaje, acceder al formulario y enviar datos
    """
    if request.method == 'POST':
        name = request.form['namecontact']
        email = request.form['emailcontact']
        subject = request.form['subjectcontact']
        message = request.form['messagecontact']
        nuevo = mensajes(name, email, subject, message, None)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.route('/modulo',methods=['GET', 'POST'])
def modulo():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte del dia'
        message = 'Se ha realizado un reporte general del dia'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    return render_template('modulo/modulo.html')

@app.route('/modulo/casa_estudio',methods=['GET', 'POST'])
def casa_estudio():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte Casa Estudio'
        message = 'Se ha realizado un reporte acerca de la casa estudio'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    return render_template('modulo/casa_estudio.html')

@app.route('/modulo/sdu3',methods=['GET', 'POST'])
def sdu3():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte SDU3'
        message = 'Se ha realizado un reporte acerca de la sala de usuarios 3'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    return render_template('modulo/sdu3.html')

@app.route('/modulo/sdu2',methods=['GET', 'POST'])
def sdu2():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte SDU2'
        message = 'Se ha realizado un reporte acerca de la sala de usuarios 2'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    return render_template('modulo/sdu2.html')

@app.route('/modulo/biblioteca',methods=['GET', 'POST'])
def biblioteca():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte Biblioteca'
        message = 'Se ha realizado un reporte acerca de la Biblioteca'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    
    return render_template('modulo/biblioteca.html')

@app.route('/modulo/6k',methods=['GET', 'POST'])
def sala6k():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte Sala 6K'
        message = 'Se ha realizado un reporte acerca de la Sala 6K'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    return render_template('modulo/6k.html')

@app.route('/modulo/5k',methods=['GET', 'POST'])
def sala5k():
    """Ruta acceder a los reportes y obetner la imagen, y enviar datos
    """
    if request.method == 'POST':
        name = 'Administrador'
        email ='admin@gmail.com'
        subject = 'Reporte Sala 5K'
        message = 'Se ha realizado un reporte acerca de la Sala 5K'
        attach = generarIMG()
        nuevo = mensajes(name, email, subject, message, attach)
        nuevo.enviar()
        Registro_Diario.agregar_elemento(nuevo)
    return render_template('modulo/5k.html')


@app.route('/logout',methods=['GET', 'POST'])
def logout():
    """Ruta para cerrar sesión
    """
    return redirect(url_for('index'))


@app.route('/home/<nombre>')
def home(nombre):
    """Ruta para acceder a la busqueda de espacios
    """
    return render_template('home.html', nombre = nombre)

def status_401(error):
    """funcion para definir el error 401
    """
    return redirect(url_for('login'))

def status_404(error):
    """funcion para definir el error 404
    """
    return "<h1>Página no encontrada</h1>", 404


# Iniciar la aplicación
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()