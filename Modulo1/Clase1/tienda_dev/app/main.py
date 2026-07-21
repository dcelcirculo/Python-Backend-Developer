from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import CategoriaNoEncontrada, ProveedorNoEncontrado
from app.routers import producto_router, categoria_router

app = FastAPI()


@app.exception_handler(CategoriaNoEncontrada)
def manejar_categoria_no_encontrada(request: Request, exc: CategoriaNoEncontrada):
    return JSONResponse(
        status_code=404,
        content={"error": str(exc)},
    )


@app.exception_handler(ProveedorNoEncontrado)
def manejar_proveedor_no_encontrado(request: Request, exc: ProveedorNoEncontrado):
    return JSONResponse(
        status_code=404,
        content={"error": "recurso_no_encontrado", "detalle": str(exc)},
    )

app.include_router(producto_router.router)
app.include_router(categoria_router.router)