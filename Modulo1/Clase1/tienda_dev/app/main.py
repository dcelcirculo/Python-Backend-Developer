from fastapi import FastAPI
from app.routers import producto_router
from app.routers import categoria_router


app = FastAPI(
    title="Tienda Dev Senior",
    description="API Backend profesional - Dev Senior",
    version="1.0.0"
)

app.include_router(producto_router.router)
app.include_router(categoria_router.router)