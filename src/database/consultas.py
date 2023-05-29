""" Consultas de sql
"""
#Librerias
import sqlite3

# Establecer conexión con la base de datos
conn = sqlite3.connect('src/database/databa.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ejecutar la sentencia SQL
sql = 'INSERT INTO Usuarios (username, password, fullname) VALUES (?, ?, ?)'
values = ("admin","pbkdf2:sha256:260000$pAmFG2lD6CusPrX8$d68f589ccf0c8d51a4914bffeaa2bc8d7a1f84d105f1d475d429667444f4ed0c","Administrador")
cursor.execute(sql, values)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()