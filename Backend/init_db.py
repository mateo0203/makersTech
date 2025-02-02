import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    marca TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    descripcion TEXT NOT NULL
)
''')

# Insertar datos iniciales
productos = [
    ('Laptop HP', 'Laptop', 'HP', 1200, 10,
     'Laptop con pantalla de 15.6 pulgadas, procesador i7, 16GB RAM.'),
    ('Laptop Dell', 'Laptop', 'Dell', 1100, 5,
     'Laptop con pantalla de 14 pulgadas, procesador i5, 8GB RAM.'),
    ('Laptop Apple', 'Laptop', 'Apple', 2000, 3,
     'MacBook Air con pantalla Retina, M1 chip, 8GB RAM.'),
    ('Teclado mecánico', 'Teclado', 'Logitech', 100, 50,
     'Teclado mecánico con retroiluminación RGB, switches Cherry MX.'),
    ('Teclado inalámbrico', 'Teclado', 'Microsoft', 40, 30,
     'Teclado inalámbrico con teclas silenciosas y batería de larga duración.'),
    ('Mouse óptico', 'Mouse', 'Logitech', 25, 100,
     'Mouse óptico ergonómico, con 3 botones y rueda de desplazamiento.'),
    ('Mouse inalámbrico', 'Mouse', 'HP', 30, 60,
     'Mouse inalámbrico con sensor óptico de alta precisión.'),
    ('Monitor 24"', 'Monitor', 'Samsung', 250, 15,
     'Monitor de 24 pulgadas, resolución Full HD, 60Hz.'),
]

cursor.executemany(
    'INSERT INTO productos (nombre, tipo, marca, precio, cantidad, descripcion) VALUES (?, ?, ?, ?, ?, ?)', productos)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos iniciales insertados correctamente.")
