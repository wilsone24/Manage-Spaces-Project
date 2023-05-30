#Librerias
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class admin(UserMixin):

    def __init__(self, id:int, username:str, password:str) -> None:
        """Constructor de la clase User

        Args:
            id (int): Identificador del admin
            username (str): Nombre de usuario
            password (str): Contraseña
        """
        self.id = id
        self.username = username
        self.password = password
        self.fullname = 'Administrador'

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
    
