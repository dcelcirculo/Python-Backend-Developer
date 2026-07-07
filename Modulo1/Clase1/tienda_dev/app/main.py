from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="Tienda Dev Senior",
    description="API Backend profesional - Dev Senior",
    version="1.0.0"
)