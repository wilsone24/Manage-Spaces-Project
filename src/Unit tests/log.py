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
    def login(self,user)->None:
        """Función para realizar el login de un usuario

        Args:
            user (): Usuario a buscar

        Raises:
            Exception: excepción al realizar la consulta
        """
        try:
            conn = open_connection()
            query = "SELECT id, username, password, fullname FROM Usuarios WHERE username = ?"
            params = (user.username,)
            row = perform_query(conn, query, params)
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            close_connection(conn)


## Unit tests
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.user1 = User(0, "carlosl","carlos1234")
        self.user2 = User(0, "paulab","paula1234")
    
    def test_login1(self):
        resultado = ModelUser.login(self.user1)
        self.assertEqual(resultado.username, "carlosl")

    def test_login11(self):
        resultado = ModelUser.login(self.user1)
        self.assertEqual(resultado.password, True)

    def test_login2(self):
        resultado = ModelUser.login(self.user2)
        self.assertEqual(resultado.username, "paulab")

    def test_login22(self):
        resultado = ModelUser.login(self.user2)
        self.assertEqual(resultado.password, True)

if __name__ == '__main__':
    unittest.main()