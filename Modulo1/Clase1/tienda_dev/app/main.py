from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Tienda Dev Senior",
    description="API Backend profesional - Dev Senior",
    version="1.0.0"
)

# Contador que recuerda cuál es el próximo ID a asignar.
# Vive fuera de los endpoints para "recordar" entre una petición y otra.
contador_id = 101

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    categoria: str   # ← línea nueva
    
productos_db = [
  { "id": 1, "nombre": "Laptop Dell Inspiron 15", "precio": 1299.99, "stock": 15, "categoria": "tecnologia" },
  { "id": 2, "nombre": "Laptop HP Pavilion", "precio": 1149.99, "stock": 12, "categoria": "tecnologia" },
  { "id": 3, "nombre": "Monitor LG 27 Pulgadas", "precio": 329.99, "stock": 20, "categoria": "tecnologia" },
  { "id": 4, "nombre": "Teclado Mecánico Redragon", "precio": 69.99, "stock": 40, "categoria": "tecnologia" },
  { "id": 5, "nombre": "Mouse Logitech G502", "precio": 59.99, "stock": 35, "categoria": "tecnologia" },
  { "id": 6, "nombre": "Disco SSD Samsung 1TB", "precio": 119.99, "stock": 25, "categoria": "tecnologia" },
  { "id": 7, "nombre": "Memoria RAM Corsair 16GB", "precio": 79.99, "stock": 18, "categoria": "tecnologia" },
  { "id": 8, "nombre": "Impresora Epson EcoTank", "precio": 289.99, "stock": 10, "categoria": "tecnologia" },
  { "id": 9, "nombre": "Tablet Samsung Galaxy Tab", "precio": 449.99, "stock": 14, "categoria": "tecnologia" },
  { "id": 10, "nombre": "Audífonos Sony WH-1000XM5", "precio": 399.99, "stock": 16, "categoria": "tecnologia" },

  { "id": 11, "nombre": "Silla Ergonómica", "precio": 249.99, "stock": 18, "categoria": "oficina" },
  { "id": 12, "nombre": "Escritorio Ejecutivo", "precio": 399.99, "stock": 8, "categoria": "oficina" },
  { "id": 13, "nombre": "Archivador Metálico", "precio": 159.99, "stock": 11, "categoria": "oficina" },
  { "id": 14, "nombre": "Lámpara de Escritorio LED", "precio": 39.99, "stock": 30, "categoria": "oficina" },
  { "id": 15, "nombre": "Calculadora Científica", "precio": 24.99, "stock": 50, "categoria": "oficina" },
  { "id": 16, "nombre": "Agenda Ejecutiva", "precio": 19.99, "stock": 60, "categoria": "oficina" },
  { "id": 17, "nombre": "Grapadora Profesional", "precio": 14.99, "stock": 45, "categoria": "oficina" },
  { "id": 18, "nombre": "Perforadora Metálica", "precio": 17.99, "stock": 28, "categoria": "oficina" },
  { "id": 19, "nombre": "Pizarra Blanca", "precio": 89.99, "stock": 12, "categoria": "oficina" },
  { "id": 20, "nombre": "Silla de Visita", "precio": 99.99, "stock": 20, "categoria": "oficina" },

  { "id": 21, "nombre": "Camiseta Deportiva", "precio": 24.99, "stock": 50, "categoria": "ropa" },
  { "id": 22, "nombre": "Jeans Azul Hombre", "precio": 49.99, "stock": 35, "categoria": "ropa" },
  { "id": 23, "nombre": "Chaqueta Impermeable", "precio": 89.99, "stock": 22, "categoria": "ropa" },
  { "id": 24, "nombre": "Sudadera con Capucha", "precio": 54.99, "stock": 30, "categoria": "ropa" },
  { "id": 25, "nombre": "Vestido Casual", "precio": 59.99, "stock": 18, "categoria": "ropa" },
  { "id": 26, "nombre": "Zapatos Deportivos", "precio": 99.99, "stock": 25, "categoria": "ropa" },
  { "id": 27, "nombre": "Sandalias", "precio": 29.99, "stock": 40, "categoria": "ropa" },
  { "id": 28, "nombre": "Gorra Ajustable", "precio": 19.99, "stock": 55, "categoria": "ropa" },
  { "id": 29, "nombre": "Bufanda de Lana", "precio": 22.99, "stock": 20, "categoria": "ropa" },
  { "id": 30, "nombre": "Guantes Térmicos", "precio": 18.99, "stock": 24, "categoria": "ropa" },

  { "id": 31, "nombre": "Café Molido Premium", "precio": 12.99, "stock": 80, "categoria": "alimentos" },
  { "id": 32, "nombre": "Arroz Integral 1kg", "precio": 4.99, "stock": 120, "categoria": "alimentos" },
  { "id": 33, "nombre": "Pasta Espagueti", "precio": 2.99, "stock": 100, "categoria": "alimentos" },
  { "id": 34, "nombre": "Aceite de Oliva", "precio": 14.99, "stock": 35, "categoria": "alimentos" },
  { "id": 35, "nombre": "Azúcar Morena", "precio": 3.99, "stock": 75, "categoria": "alimentos" },
  { "id": 36, "nombre": "Sal Marina", "precio": 2.49, "stock": 90, "categoria": "alimentos" },
  { "id": 37, "nombre": "Harina de Trigo", "precio": 3.49, "stock": 65, "categoria": "alimentos" },
  { "id": 38, "nombre": "Galletas Integrales", "precio": 5.99, "stock": 70, "categoria": "alimentos" },
  { "id": 39, "nombre": "Chocolate Amargo", "precio": 6.99, "stock": 45, "categoria": "alimentos" },
  { "id": 40, "nombre": "Miel Natural", "precio": 11.99, "stock": 28, "categoria": "alimentos" },

  { "id": 41, "nombre": "Sofá de Tres Puestos", "precio": 899.99, "stock": 6, "categoria": "hogar" },
  { "id": 42, "nombre": "Mesa de Centro", "precio": 179.99, "stock": 14, "categoria": "hogar" },
  { "id": 43, "nombre": "Comedor para 6 Personas", "precio": 799.99, "stock": 5, "categoria": "hogar" },
  { "id": 44, "nombre": "Lámpara de Piso", "precio": 89.99, "stock": 18, "categoria": "hogar" },
  { "id": 45, "nombre": "Cortinas Blackout", "precio": 59.99, "stock": 22, "categoria": "hogar" },
  { "id": 46, "nombre": "Almohada Viscoelástica", "precio": 34.99, "stock": 40, "categoria": "hogar" },
  { "id": 47, "nombre": "Cobija Térmica", "precio": 44.99, "stock": 27, "categoria": "hogar" },
  { "id": 48, "nombre": "Juego de Sábanas Queen", "precio": 69.99, "stock": 25, "categoria": "hogar" },
  { "id": 49, "nombre": "Estantería de Madera", "precio": 159.99, "stock": 10, "categoria": "hogar" },
  { "id": 50, "nombre": "Espejo Decorativo", "precio": 79.99, "stock": 12, "categoria": "hogar" },

  { "id": 51, "nombre": "Balón de Fútbol", "precio": 29.99, "stock": 30, "categoria": "deportes" },
  { "id": 52, "nombre": "Raqueta de Tenis", "precio": 149.99, "stock": 15, "categoria": "deportes" },
  { "id": 53, "nombre": "Mancuernas 10kg", "precio": 79.99, "stock": 20, "categoria": "deportes" },
  { "id": 54, "nombre": "Colchoneta de Yoga", "precio": 34.99, "stock": 25, "categoria": "deportes" },
  { "id": 55, "nombre": "Bicicleta Montaña", "precio": 699.99, "stock": 8, "categoria": "deportes" },
  { "id": 56, "nombre": "Casco Deportivo", "precio": 49.99, "stock": 18, "categoria": "deportes" },
  { "id": 57, "nombre": "Botella Térmica", "precio": 24.99, "stock": 40, "categoria": "deportes" },
  { "id": 58, "nombre": "Guantes para Gimnasio", "precio": 19.99, "stock": 32, "categoria": "deportes" },
  { "id": 59, "nombre": "Cuerda para Saltar", "precio": 14.99, "stock": 45, "categoria": "deportes" },
  { "id": 60, "nombre": "Balón de Baloncesto", "precio": 34.99, "stock": 26, "categoria": "deportes" },

  { "id": 61, "nombre": "Shampoo Anticaspa", "precio": 9.99, "stock": 50, "categoria": "belleza" },
  { "id": 62, "nombre": "Acondicionador Hidratante", "precio": 10.99, "stock": 42, "categoria": "belleza" },
  { "id": 63, "nombre": "Crema Facial", "precio": 18.99, "stock": 35, "categoria": "belleza" },
  { "id": 64, "nombre": "Protector Solar SPF50", "precio": 16.99, "stock": 30, "categoria": "belleza" },
  { "id": 65, "nombre": "Perfume Masculino", "precio": 69.99, "stock": 15, "categoria": "belleza" },
  { "id": 66, "nombre": "Perfume Femenino", "precio": 74.99, "stock": 16, "categoria": "belleza" },
  { "id": 67, "nombre": "Cepillo Eléctrico Facial", "precio": 39.99, "stock": 12, "categoria": "belleza" },
  { "id": 68, "nombre": "Kit de Maquillaje", "precio": 59.99, "stock": 18, "categoria": "belleza" },
  { "id": 69, "nombre": "Secador de Cabello", "precio": 49.99, "stock": 20, "categoria": "belleza" },
  { "id": 70, "nombre": "Plancha para Cabello", "precio": 54.99, "stock": 15, "categoria": "belleza" },

  { "id": 71, "nombre": "Taladro Inalámbrico", "precio": 129.99, "stock": 14, "categoria": "ferreteria" },
  { "id": 72, "nombre": "Martillo de Acero", "precio": 19.99, "stock": 35, "categoria": "ferreteria" },
  { "id": 73, "nombre": "Destornillador Phillips", "precio": 9.99, "stock": 60, "categoria": "ferreteria" },
  { "id": 74, "nombre": "Llave Inglesa", "precio": 24.99, "stock": 25, "categoria": "ferreteria" },
  { "id": 75, "nombre": "Caja de Herramientas", "precio": 49.99, "stock": 18, "categoria": "ferreteria" },
  { "id": 76, "nombre": "Sierra Manual", "precio": 29.99, "stock": 20, "categoria": "ferreteria" },
  { "id": 77, "nombre": "Nivel de Burbuja", "precio": 14.99, "stock": 28, "categoria": "ferreteria" },
  { "id": 78, "nombre": "Cinta Métrica 5m", "precio": 12.99, "stock": 40, "categoria": "ferreteria" },
  { "id": 79, "nombre": "Juego de Brocas", "precio": 34.99, "stock": 22, "categoria": "ferreteria" },
  { "id": 80, "nombre": "Alicate Universal", "precio": 17.99, "stock": 31, "categoria": "ferreteria" },

  { "id": 81, "nombre": "Lego Classic", "precio": 59.99, "stock": 18, "categoria": "juguetes" },
  { "id": 82, "nombre": "Muñeca Interactiva", "precio": 49.99, "stock": 20, "categoria": "juguetes" },
  { "id": 83, "nombre": "Carro a Control Remoto", "precio": 69.99, "stock": 16, "categoria": "juguetes" },
  { "id": 84, "nombre": "Rompecabezas 1000 Piezas", "precio": 24.99, "stock": 30, "categoria": "juguetes" },
  { "id": 85, "nombre": "Peluche Gigante", "precio": 39.99, "stock": 14, "categoria": "juguetes" },
  { "id": 86, "nombre": "Juego de Mesa Monopoly", "precio": 34.99, "stock": 20, "categoria": "juguetes" },
  { "id": 87, "nombre": "Ajedrez de Madera", "precio": 29.99, "stock": 12, "categoria": "juguetes" },
  { "id": 88, "nombre": "Patineta", "precio": 79.99, "stock": 10, "categoria": "juguetes" },
  { "id": 89, "nombre": "Scooter Infantil", "precio": 89.99, "stock": 9, "categoria": "juguetes" },
  { "id": 90, "nombre": "Kit de Ciencia", "precio": 44.99, "stock": 15, "categoria": "juguetes" },

  { "id": 91, "nombre": "Smartwatch Garmin", "precio": 299.99, "stock": 13, "categoria": "tecnologia" },
  { "id": 92, "nombre": "Cámara Web Full HD", "precio": 89.99, "stock": 21, "categoria": "tecnologia" },
  { "id": 93, "nombre": "Router WiFi 6", "precio": 149.99, "stock": 17, "categoria": "tecnologia" },
  { "id": 94, "nombre": "Power Bank 20000mAh", "precio": 49.99, "stock": 34, "categoria": "tecnologia" },
  { "id": 95, "nombre": "Cargador Inalámbrico", "precio": 29.99, "stock": 27, "categoria": "tecnologia" },
  { "id": 96, "nombre": "Memoria USB 128GB", "precio": 24.99, "stock": 60, "categoria": "tecnologia" },
  { "id": 97, "nombre": "Cable HDMI 2 Metros", "precio": 14.99, "stock": 80, "categoria": "tecnologia" },
  { "id": 98, "nombre": "Micrófono USB", "precio": 99.99, "stock": 15, "categoria": "tecnologia" },
  { "id": 99, "nombre": "Parlante Bluetooth", "precio": 79.99, "stock": 19, "categoria": "tecnologia" },
  { "id": 100, "nombre": "Proyector Portátil", "precio": 349.99, "stock": 8, "categoria": "tecnologia" }
]
    
@app.get("/")
def raiz():
    return{
        "mensaje": "Bienvenido a la API de Tienda Dev Senior",
        "version":"1.0.0"
    }
    
@app.get("/productos")
def listar_productos(categoria: str | None = None, precio_max: float | None = None):
    resultado = productos_db
    if categoria is not None:
        resultado = [p for p in resultado if p["categoria"].lower() == categoria.lower()]
    if precio_max is not None:
        resultado = [p for p in resultado if p["precio"] <= precio_max]
    return {"total": len(resultado), "productos": resultado}
    
@app.get("/productos/{producto_id}")
def obtener_producto_id(producto_id: int):
    for p in productos_db:
        if p["id"] == producto_id:
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/productos")
def crear_producto(producto: ProductoCreate):
    global contador_id
    nuevo = {
        "id": contador_id,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "stock": producto.stock,
        "categoria": producto.categoria
    }
    productos_db.append(nuevo)
    contador_id += 1
    return {"mensaje": "Producto creado exitosamente", "producto": nuevo}

@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, datos: ProductoCreate):
    for p in productos_db:
        if p["id"] == producto_id:
            p["nombre"] = datos.nombre
            p["precio"] = datos.precio
            p["stock"] = datos.stock
            p["categoria"] = datos.categoria
            return {"mensaje": "Producto actualizado", "producto": p}
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    for p in productos_db:
        if p["id"] == producto_id:
            productos_db.remove(p)
            return {"mensaje": f"Producto {producto_id} eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")