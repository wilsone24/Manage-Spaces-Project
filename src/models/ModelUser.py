from .entities.User import User
import sqlite3

def open_connection():
    conn = sqlite3.connect('src/database/databa.db')
    return conn

def close_connection(conn):
    conn.close()

def perform_query(conn, query, params):
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    cursor.close()
    return result

class ModelUser():
    @classmethod
    def login(self,user):
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
    def get_by_id(self, id):
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
    def register(self,params):
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

