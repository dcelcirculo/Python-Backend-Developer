categorias_db = []
contador_id = 1

def crear_categoria(datos):
    global contador_id
    nueva = {
        "id": contador_id,
        "nombre": datos.nombre
    }
    categorias_db.append(nueva)
    contador_id += 1
    return nueva


def listar_categorias():
    return categorias_db


def obtener_categoria(categoria_id):
    for c in categorias_db:
        if c["id"] == categoria_id:
            return c
    return None


def actualizar_categoria(categoria_id, datos):
    for c in categorias_db:
        if c["id"] == categoria_id:
            c["nombre"] = datos.nombre
            return c
    return None


def eliminar_categoria(categoria_id):
    for c in categorias_db:
        if c["id"] == categoria_id:
            categorias_db.remove(c)
            return True
    return False