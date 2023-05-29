#Librerias
from .entities.User import User
import sqlite3

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

    @classmethod
    def get_by_id(self, id)->None:
        """Función para obtener un usuario por su id

        Args:
            id (): identificador del usuario

        Raises:
            Exception: excepción al realizar el query

        """
        try:
            conn = open_connection()
            query = "SELECT id, username, fullname FROM Usuarios WHERE id = ?"
            params = (id,)
            row = perform_query(conn, query, params)
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            close_connection(conn)

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

