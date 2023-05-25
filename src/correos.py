import yagmail

email = 'wilson.estrada2407@gmail.com'
contraseña = 'chixnmiklhbrdcnj'

yag = yagmail.SMTP(user = email, password = contraseña)
destinatarios = ['dfbarbosa@uninorte.edu.co','wilson.estrada2407@gmail.com','dianabarbosa0918@gmail.com']

class mensajes():
    def __init__(self, nombre, correo, asunto, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.asunto = asunto
        self.mensaje = mensaje

    def enviar(self):
        yag.send(destinatarios, self.asunto, f"Nombre: {self.nombre}\nCorreo: {self.correo}\nMensaje: {self.mensaje}")
        return True

listamen = dict({})