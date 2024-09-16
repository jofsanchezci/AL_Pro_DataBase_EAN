import sqlite3

# Conectar a la base de datos existente
conn = sqlite3.connect('mi_base_de_datos_2.db')
cursor = conn.cursor()

# Consulta para contar la cantidad de personas por género
cursor.execute('''
    SELECT sex, COUNT(*) as cantidad
    FROM usuarios
    GROUP BY sex
''')

# Obtener y mostrar los resultados
resultados = cursor.fetchall()

for fila in resultados:
    print(f"Género: {fila[0]}, Cantidad: {fila[1]}")

# Cerrar la conexión
conn.close()
