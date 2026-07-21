from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tienda API", description="API para gestionar productos y categorías", version="1.0.0")

inventario_db = [
    {"id": 1, "nombre": "Producto A", "precio": 10.0},
    {"id": 2, "nombre": "Producto B", "precio": 20.0}
]

class Producto(BaseModel):
    nombre: str
    precio: float
    
@app.get("/api/productos")
def listar_productos():
    return inventario_db

@app.post("/api/productos")
def crear_producto(nuevo_producto: Producto):
    nuevo_id = len(inventario_db) + 1
    producto_dict = nuevo_producto.model_dump()
    producto_dict["id"] = nuevo_id
    inventario_db.append(producto_dict)
    return {"mensaje": "Producto creado exitosamente", "producto": producto_dict}
