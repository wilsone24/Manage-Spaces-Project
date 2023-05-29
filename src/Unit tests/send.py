#Librerias
import unittest
import yagmail

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
    


## Unit tests
class TestSend(unittest.TestCase):
    def setUp(self):
        self.nuevo1 = mensajes("Felipe","felipe@gmail.com","Prueba","Esto es una prueba",None)
        self.nuevo2 = mensajes("Margarita","margarita@gmail.com","Prueba","Esto es una prueba",None)
    
    def test_send1(self):
        resultado = self.nuevo1.enviar()
        self.assertEqual(resultado, True)

    def test_send2(self):
        resultado = self.nuevo2.enviar()
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()