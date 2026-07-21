# Contador que recuerda cuál es el próximo ID a asignar.
# Vive fuera de los endpoints para "recordar" entre una petición y otra.
   
contador_id = 101
    
productos_db = [
  {
    "id": 1,
    "nombre": "Laptop Dell Inspiron 15",
    "precio": 1299.99,
    "precio_oferta": 1104.99,
    "stock": 15,
    "categoria": "tecnologia"
  },
  {
    "id": 2,
    "nombre": "Laptop HP Pavilion",
    "precio": 1149.99,
    "precio_oferta": 1034.99,
    "stock": 12,
    "categoria": "tecnologia"
  },
  {
    "id": 11,
    "nombre": "Silla Ergonómica",
    "precio": 249.99,
    "precio_oferta": 212.49,
    "stock": 18,
    "categoria": "oficina"
  },
  {
    "id": 22,
    "nombre": "Jeans Azul Hombre",
    "precio": 49.99,
    "precio_oferta": 44.99,
    "stock": 35,
    "categoria": "ropa"
  },
  {
    "id": 31,
    "nombre": "Café Molido Premium",
    "precio": 12.99,
    "precio_oferta": 11.04,
    "stock": 80,
    "categoria": "alimentos"
  },
  {
    "id": 32,
    "nombre": "Arroz Integral 1kg",
    "precio": 4.99,
    "precio_oferta": 4.49,
    "stock": 120,
    "categoria": "alimentos"
  },
  {
    "id": 49,
    "nombre": "Estantería de Madera",
    "precio": 159.99,
    "precio_oferta": 135.99,
    "stock": 10,
    "categoria": "hogar"
  },
  {
    "id": 50,
    "nombre": "Espejo Decorativo",
    "precio": 79.99,
    "precio_oferta": 71.99,
    "stock": 12,
    "categoria": "hogar"
  },
  {
    "id": 51,
    "nombre": "Balón de Fútbol",
    "precio": 29.99,
    "precio_oferta": 28.99,
    "stock": 30,
    "categoria": "deportes"
  },
  {
    "id": 52,
    "nombre": "Raqueta de Tenis",
    "precio": 149.99,
    "precio_oferta": 134.99,
    "stock": 15,
    "categoria": "deportes"
  },
  {
    "id": 69,
    "nombre": "Secador de Cabello",
    "precio": 49.99,
    "precio_oferta": 39.99,
    "stock": 20,
    "categoria": "belleza"
  },
  {
    "id": 70,
    "nombre": "Plancha para Cabello",
    "precio": 54.99,
    "precio_oferta": 49.49,
    "stock": 15,
    "categoria": "belleza"
  },
  {
    "id": 71,
    "nombre": "Taladro Inalámbrico",
    "precio": 129.99,
    "precio_oferta": 110.49,
    "stock": 14,
    "categoria": "ferreteria"
  },
  {
    "id": 72,
    "nombre": "Martillo de Acero",
    "precio": 19.99,
    "precio_oferta": 18.99,
    "stock": 35,
    "categoria": "ferreteria"
  },
  {
    "id": 89,
    "nombre": "Scooter Infantil",
    "precio": 89.99,
    "precio_oferta": 76.49,
    "stock": 9,
    "categoria": "juguetes"
  },
  {
    "id": 90,
    "nombre": "Kit de Ciencia",
    "precio": 44.99,
    "precio_oferta": 43.99,
    "stock": 15,
    "categoria": "juguetes"
  },
  {
    "id": 91,
    "nombre": "Smartwatch Garmin",
    "precio": 299.99,
    "precio_oferta": 254.99,
    "stock": 13,
    "categoria": "tecnologia"
  },
  {
    "id": 92,
    "nombre": "Cámara Web Full HD",
    "precio": 89.99,
    "precio_oferta": 80.99,
    "stock": 21,
    "categoria": "tecnologia"
  }
]

def crear_producto(datos):
    global contador_id
    nuevo = {
        "id": contador_id,
        "nombre": datos.nombre,
        "precio": datos.precio,
        #"precio_oferta": datos.precio_oferta,
        "stock": datos.stock,
        "categoria": datos.categoria
    }
    productos_db.append(nuevo)
    contador_id += 1
    return nuevo


def actualizar_parcial_producto(producto_id, datos):
    for p in productos_db:
        if p["id"] == producto_id:
            cambios = datos.model_dump(exclude_unset=True)
            for campo, valor in cambios.items():
                p[campo] = valor
            return p
    return None


def listar_productos(categoria=None, precio_max=None):
    resultado = productos_db
    if categoria is not None:
        resultado = [p for p in resultado if p["categoria"].lower() == categoria.lower()]
    if precio_max is not None:
        resultado = [p for p in resultado if p["precio"] <= precio_max]
    return resultado

def obtener_producto(producto_id):
    for p in productos_db:
        if p["id"] == producto_id:
            return p
    return None

def actualizar_producto(producto_id, datos):
    for p in productos_db:
        if p["id"] == producto_id:
            p["nombre"] = datos.nombre
            p["precio"] = datos.precio
            p["stock"] = datos.stock
            p["categoria"] = datos.categoria
            return p
    return None


def eliminar_producto(producto_id):
    for p in productos_db:
        if p["id"] == producto_id:
            productos_db.remove(p)
            return True
    return False