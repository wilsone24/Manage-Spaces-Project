""" import sqlite3

# Establecer conexión con la base de datos
conn = sqlite3.connect('src/database/databa.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ejecutar la sentencia SQL
sql = 'INSERT INTO Usuarios (username, password, fullname) VALUES (?, ?, ?)'
values = ("dfbarbosa","pbkdf2:sha256:260000$VO7X393eV1trS9XT$893b01eedf0c33b0d0269180bfeabfda8b31f9180dd1d933c8134d06a4e84408","Diana Barbosa")
cursor.execute(sql, values)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close() """