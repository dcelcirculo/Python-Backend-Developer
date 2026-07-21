from app.exceptions import CategoriaNoEncontrada

categorias = []
contador_id = 1

def crear_categoria(datos):
    global contador_id
    nueva = {
        "id": contador_id,
        "nombre": datos.nombre
    }
    categorias.append(nueva)
    contador_id += 1
    return nueva


def listar_categorias():
    return categorias


def obtener_categoria(categoria_id: int):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            return categoria
    raise CategoriaNoEncontrada(categoria_id)


def actualizar_categoria(categoria_id, datos):
    for c in categorias:
        if c["id"] == categoria_id:
            c["nombre"] = datos.nombre
            return c
    # return None
    return CategoriaNoEncontrada(categoria_id)


def eliminar_categoria(categoria_id):
    for c in categorias:
        if c["id"] == categoria_id:
            categorias.remove(c)
            return True
    return False