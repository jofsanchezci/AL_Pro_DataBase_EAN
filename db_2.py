import sqlite3
import pandas as pd


file_path = 'data.xlsx' 
data = pd.read_excel(file_path)

# Conectar o crear la base de datos
conn = sqlite3.connect('mi_base_de_datos_2.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        edad INTEGER,
        nivel_edu TEXT,
        ingreso_mensual REAL,
        sex TEXT,
        anios_esc INTEGER)
''')

# Insertar datos
for index, row in data.iterrows():
    cursor.execute('''
        INSERT INTO usuarios (id, edad, nivel_edu, ingreso_mensual, sex, anios_esc)
        VALUES (?, ?, ?, ?, ?, ?)''', 
        (row['id'], row['edad'], row['nivel_edu'], row['ingreso_mensual'], row['sex'], row['anios_esc']))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos insertados correctamente en la base de datos.")
