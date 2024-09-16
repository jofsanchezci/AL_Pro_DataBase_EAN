
# Persistencia de Datos con SQLite en Python

Este proyecto demuestra cómo usar `sqlite3` en Python para persistir datos usando SQLite, una base de datos ligera que almacena los datos en un archivo local.

## Requisitos
- Python 3.x

SQLite viene preinstalado en Python, por lo que no se requieren dependencias adicionales.

## Pasos

### 1. Conectar a la Base de Datos

Primero, necesitas establecer una conexión con la base de datos. Si la base de datos no existe, se creará automáticamente en el archivo especificado.

```python
import sqlite3

# Conectar a la base de datos (si no existe, se creará)
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()
```

### 2. Crear una Tabla

Puedes crear una tabla con la estructura que desees. En este ejemplo, crearemos una tabla `usuarios` que almacena el `id`, `nombre` y `edad`.

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL)
''')

# Guardar los cambios
conn.commit()
```

### 3. Insertar Datos

Para insertar datos en la tabla:

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 25))
conn.commit()
```

### 4. Consultar Datos

Puedes consultar los datos con una sentencia SQL `SELECT`:

```python
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)
```

### 5. Actualizar y Eliminar Datos

#### Actualizar:

```python
cursor.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", ("Carlos", 1))
conn.commit()
```

#### Eliminar:

```python
cursor.execute("DELETE FROM usuarios WHERE id = ?", (1,))
conn.commit()
```

### 6. Cerrar la Conexión

Es importante cerrar la conexión para liberar los recursos:

```python
conn.close()
```

## Ejemplo Completo

```python
import sqlite3

# Conectar a la base de datos
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
```


# Introducción a Pandas en Python

Pandas es una biblioteca de Python utilizada para la manipulación y análisis de datos. Está diseñada para trabajar con grandes volúmenes de datos de manera eficiente y proporciona dos estructuras principales: `Series` y `DataFrame`.

## Estructuras de datos en Pandas

### Series
Una `Serie` es una estructura unidimensional similar a un array. Cada valor tiene un índice que lo identifica.

```python
import pandas as pd

# Crear una serie de ejemplo
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(serie)
```

### DataFrame
Un `DataFrame` es una estructura bidimensional (como una tabla). Puedes acceder a las filas o columnas por nombre o índice.

```python
# Crear un DataFrame a partir de un diccionario
data = {
    'nombre': ['Ana', 'Luis', 'Carlos'],
    'edad': [22, 35, 58],
    'ciudad': ['Bogotá', 'Medellín', 'Cali']
}

df = pd.DataFrame(data)
print(df)
```

## Operaciones comunes en Pandas

### Leer y escribir datos
Pandas permite leer datos desde diferentes formatos y exportarlos de manera sencilla.

```python
# Leer un archivo CSV
df = pd.read_csv('archivo.csv')

# Guardar un DataFrame como archivo CSV
df.to_csv('salida.csv', index=False)
```

### Seleccionar datos
Puedes seleccionar columnas, filas o celdas específicas en un DataFrame.

```python
# Seleccionar una columna
print(df['nombre'])

# Seleccionar una fila por índice
print(df.iloc[0])
```

### Filtrar datos
Puedes aplicar condiciones para filtrar filas en un DataFrame.

```python
# Filtrar personas mayores de 30 años
mayores_de_30 = df[df['edad'] > 30]
print(mayores_de_30)
```

### Operaciones sobre columnas
Puedes realizar operaciones matemáticas sobre columnas y aplicar funciones.

```python
# Añadir una nueva columna
df['edad_en_dias'] = df['edad'] * 365

# Calcular el promedio de la columna 'edad'
promedio_edad = df['edad'].mean()
print(promedio_edad)
```

### Agrupar datos
Usando `groupby()`, puedes agrupar los datos y aplicar operaciones agregadas.

```python
# Agrupar por 'ciudad' y calcular el promedio de edad
promedio_edad_por_ciudad = df.groupby('ciudad')['edad'].mean()
print(promedio_edad_por_ciudad)
```

### Limpiar y transformar datos
Puedes manejar valores faltantes y transformar datos.

```python
# Reemplazar valores nulos
df.fillna(0, inplace=True)

# Eliminar filas con valores nulos
df.dropna(inplace=True)
```

## Flujo típico de trabajo con Pandas

1. **Cargar los datos**: Leer datos desde diferentes fuentes.
2. **Explorar los datos**: Usar funciones como `head()`, `info()`, `describe()`.
3. **Limpiar los datos**: Manejar valores nulos, duplicados, y corregir tipos de datos.
4. **Transformar los datos**: Filtrar, agrupar y crear nuevas columnas.
5. **Visualizar o analizar los datos**: Realizar cálculos y generar gráficos.
6. **Exportar los resultados**: Guardar los datos en archivos CSV, Excel, etc.

## Ejemplo práctico

```python
import pandas as pd

# Leer archivo CSV
df = pd.read_csv('ventas.csv')

# Calcular ventas totales por vendedor
ventas_totales = df.groupby('vendedor')['venta'].sum()
print(ventas_totales)

# Guardar el resultado
ventas_totales.to_csv('ventas_totales.csv')
```

## Ejemplo de excel con Pandas
```python
import pandas as pd

# Leer el archivo Excel en un DataFrame
df = pd.read_excel('archivo.xlsx')

# Mostrar las primeras filas del DataFrame
print(df.head())
```




## Conclusión
Pandas es una biblioteca poderosa para manipulación de datos en Python. Con estructuras como `Series` y `DataFrame`, puedes realizar análisis de datos de manera rápida y eficiente.




