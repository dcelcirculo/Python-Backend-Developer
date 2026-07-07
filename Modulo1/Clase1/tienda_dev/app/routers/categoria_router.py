from fastapi import APIRouter, HTTPException
from app.schemas.categoria_schema import CategoriaCreate
from app.services import categoria_service

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/")
def crear(categoria: CategoriaCreate):
    nueva = categoria_service.crear_categoria(categoria)
    return {"mensaje": "Categoria creada exitosamente", "categoria": nueva}


@router.get("/")
def listar():
    resultado = categoria_service.listar_categorias()
    return {"total": len(resultado), "categorias": resultado}


@router.get("/{categoria_id}")
def obtener(categoria_id: int):
    categoria = categoria_service.obtener_categoria(categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria


@router.put("/{categoria_id}")
def actualizar(categoria_id: int, datos: CategoriaCreate):
    categoria = categoria_service.actualizar_categoria(categoria_id, datos)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return {"mensaje": "Categoria actualizada", "categoria": categoria}


@router.delete("/{categoria_id}")
def eliminar(categoria_id: int):
    eliminada = categoria_service.eliminar_categoria(categoria_id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return {"mensaje": f"Categoria {categoria_id} eliminada correctamente"}