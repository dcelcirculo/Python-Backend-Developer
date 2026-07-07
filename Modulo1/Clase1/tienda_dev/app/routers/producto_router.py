from fastapi import APIRouter, HTTPException
from app.schemas.producto_schema import ProductoCreate, ProductoUpdate
from app.services import producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/")
def crear(producto: ProductoCreate):
    nuevo = producto_service.crear_producto(producto)
    return {"mensaje": "Producto creado exitosamente", "producto": nuevo}


@router.get("/")
def listar(categoria: str | None = None, precio_max: float | None = None):
    resultado = producto_service.listar_productos(categoria, precio_max)
    return {"total": len(resultado), "productos": resultado}


@router.get("/{producto_id}")
def obtener(producto_id: int):
    producto = producto_service.obtener_producto(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.put("/{producto_id}")
def actualizar(producto_id: int, datos: ProductoCreate):
    producto = producto_service.actualizar_producto(producto_id, datos)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto actualizado", "producto": producto}


@router.patch("/{producto_id}")
def actualizar_parcial(producto_id: int, datos: ProductoUpdate):
    producto = producto_service.actualizar_parcial_producto(producto_id, datos)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto actualizado parcialmente", "producto": producto}


@router.delete("/{producto_id}")
def eliminar(producto_id: int):
    eliminado = producto_service.eliminar_producto(producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto {producto_id} eliminado correctamente"}