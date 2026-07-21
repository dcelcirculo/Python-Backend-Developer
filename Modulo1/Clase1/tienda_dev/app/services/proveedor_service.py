from app.exceptions import ProveedorNoEncontrado

proveedores = []

contador_id = 1

def crear_proveedor(datos):
    global contador_id
    nuevo = {
        "id": contador_id,
        "nombre": datos.nombre
    }
    proveedores.append(nuevo)
    contador_id += 1
    return nuevo


def listar_proveedores():
    return proveedores


def obtener_proveedor(proveedor_id: int):
    for proveedor in proveedores:
        if proveedor["id"] == proveedor_id:
            return proveedor
    raise ProveedorNoEncontrado(proveedor_id)


def actualizar_proveedor(proveedor_id, datos):
    for p in proveedores:
        if p["id"] == proveedor_id:
            p["nombre"] = datos.nombre
            return p
    return ProveedorNoEncontrado(proveedor_id)


def eliminar_proveedor(proveedor_id):
    for p in proveedores:
        if p["id"] == proveedor_id:
            proveedores.remove(p)
            return True
    return False