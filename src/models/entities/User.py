#Librerias
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
    
print(generate_password_hash("admin2023"))
