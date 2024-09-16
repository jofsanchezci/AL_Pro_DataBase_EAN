import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL)
''')

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 25))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Ana", 30))

# Guardar los cambios
conn.commit()

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

# Cerrar la conexión
conn.close()