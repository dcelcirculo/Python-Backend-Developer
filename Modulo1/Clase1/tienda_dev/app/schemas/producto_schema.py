from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    categoria: str   # ← línea nueva
    
    
class ProductoUpdate(BaseModel):
    #nombre: str | None = None
    precio: float | None = None
    stock: int | None = None
    categoria: str | None = None