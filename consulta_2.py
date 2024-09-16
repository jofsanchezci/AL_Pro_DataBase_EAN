import sqlite3

# Conectar a la base de datos existente
conn = sqlite3.connect('mi_base_de_datos_2.db')
cursor = conn.cursor()

# Consulta para obtener el promedio de edad por género
cursor.execute('''
    SELECT sex, AVG(edad) as promedio_edad
    FROM usuarios
    GROUP BY sex
''')

# Obtener y mostrar los resultados
resultados = cursor.fetchall()

for fila in resultados:
    print(f"Género: {fila[0]}, Promedio de Edad: {fila[1]:.2f} años")

# Cerrar la conexión
conn.close()
