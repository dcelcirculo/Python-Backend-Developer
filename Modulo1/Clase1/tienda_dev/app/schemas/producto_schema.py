from pydantic import BaseModel, Field, field_validator, model_validator


class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    precio: float = Field(..., gt=0)
    precio_oferta: float | None = Field(None, gt=0) # field es para decir que e
    stock: int = Field(..., ge=0)
    categoria: str = Field(..., min_length=3)

    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, valor: str) -> str:
        valor_limpio = valor.strip()
        if valor_limpio == "":
            raise ValueError("El nombre no puede ser solo espacios")
        return valor_limpio


    @field_validator("categoria")
    @classmethod
    def validar_categoria(cls, valor: str) -> str:
        categorias_validas = ["tecnologia", "papeleria", "hogar"]
        valor_limpio = valor.strip().lower()
        if valor_limpio not in categorias_validas:
            raise ValueError(f"Categoría inválida. Use una de: {categorias_validas}")
        return valor_limpio
    
        
    @model_validator(mode="after")
    def validar_oferta(self):
        if self.precio_oferta is not None and self.precio_oferta >= self.precio:
            raise ValueError("El precio de oferta debe ser menor al precio normal")
        return self
    
class ProductoUpdate(BaseModel):
    nombre: str | None = None
    precio: float | None = None
    precio_oferta: float | None = None
    stock: int | None = None
    categoria: str | None = None