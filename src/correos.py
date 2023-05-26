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

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class RegistroDiario:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            nodo_actual = self.cabeza
            while nodo_actual:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente

Registro_Diario = RegistroDiario()