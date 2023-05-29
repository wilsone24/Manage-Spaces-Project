#Librerias
import unittest
import sqlite3
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id:int, username:str, password:str, fullname="") -> None:
        """Constructor de la clase User

        Args:
            id (int): Identificador del usuario
            username (str): Nombre de usuario
            password (str): Contraseña
            fullname (str, optional): Nombre completo del usuario. Defaults to "".
        """
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password:str, password:str)->bool:
        """Función para verificar la contraseña

        Args:
            hashed_password (str): Contraseña encriptada
            password (str): Contraseña a verificar

        Returns:
            bool: True si la contraseña es correcta, False si no lo es
        """
        return check_password_hash(hashed_password, password)

def open_connection():
    """Función para abrir una conexión con la base de datos

    Returns:
        sqlite3.Connection: Conexión con la base de datos
    """
    conn = sqlite3.connect('src/database/databa.db')
    return conn

def close_connection(conn)->None:
    """Función para cerrar una conexión con la base de datos

    Args:
        conn (): Conexión con la base de datos
    """
    conn.close()

def perform_query(conn, query, params):
    """_summary_

    Args:
        conn (): Conexión con la base de datos
        query (): Consult a realizar
        params (): Parametros de la consulta

    Returns:
        result: Resultado de la consulta
    """
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    cursor.close()
    return result

class ModelUser():
    @classmethod
    def register(self,params)->None:
        """Función para registrar un usuario

        Args:
            params (): Parametros de la consulta

        Raises:
            Exception: excepción al realizar el query
        """
        try:
            conn = open_connection()
            query = "INSERT INTO Usuarios (username, password, fullname) VALUES (?, ?, ?)"
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            cursor.close()
            return True
        except Exception as ex:
            raise Exception(ex)
        finally:
            close_connection(conn)

## Unit tests
class TestRegister(unittest.TestCase):
    def setUp(self):
        self.values1 = ("carlosl", generate_password_hash("carlos1234"), "Carlos Lopez")
        self.values2 = ("paulab", generate_password_hash("paula1234"), "Paula Barbosa")
    
    def test_register1(self):
        resultado = ModelUser.register(self.values1)
        self.assertEqual(resultado, True)

    def test_register2(self):
        resultado = ModelUser.register(self.values2)
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()