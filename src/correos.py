#Librerias Necesarias
import yagmail
import pyautogui

#Constantes
email = 'deuxadmim@gmail.com'
contraseña = 'zyrerlkupyiujxwn'
yag = yagmail.SMTP(user = email, password = contraseña)
destinatarios = ['wilson.estrada2407@gmail.com','deuxadmim@gmail.com']



class mensajes():
    def __init__(self, nombre:str, correo:str, asunto:str, mensaje:str,adjuntos)->None :
        """Funcion constructora de la clase Mensajes

        Args:
            nombre (str): Nombre del Remitente
            correo (str): Correo del Remitente
            asunto (str): Asunto del mensaje
            mensaje (str): Cuerpo del mensaje
            adjuntos (): Archivos adjuntos
        """
        self.nombre = nombre
        self.correo = correo
        self.asunto = asunto
        self.mensaje = mensaje
        self.adjuntos = adjuntos

    def enviar(self)->bool:
        """Función para enviar el mensaje

        Returns:
            bool: Retorna true para confirmar el envio del mensaje
        """
        yag.send(destinatarios, self.asunto, f"Nombre: {self.nombre}\nCorreo: {self.correo}\nMensaje: {self.mensaje}",self.adjuntos)
        return True

class Nodo:
    def __init__(self, dato)->None:
        """Funcion constructora de la clase Nodo

        Args:
            dato (): Dato a almacenar en el nodo
        """
        self.dato = dato
        self.siguiente = None

class RegistroDiario:
    def __init__(self)->None:
        """Funcion constructora de la clase RegistroDiario
        """
        self.cabeza = None

    def agregar_elemento(self, dato)->None:
        """Función para agregar un elemento a la lista

        Args:
            dato (): Dato a agregar
        """
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir_lista(self)->None:
        """Función para imprimir la lista
        """
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            nodo_actual = self.cabeza
            while nodo_actual:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente

Registro_Diario = RegistroDiario()

def generarIMG()->str:
    """Funcion para generar una captura de pantalla

    Returns:
        str: Ruta de la imagen generada
    """
    posicion_x = 300 
    posicion_y = 150  
    ancho = 1050  
    alto = 550 
    captura = pyautogui.screenshot(region=(posicion_x, posicion_y, ancho, alto))
    ruta_captura = 'src/capturas/Reporte.png'
    captura.save(ruta_captura)
    return  ruta_captura
