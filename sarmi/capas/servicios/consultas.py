# Arma las respuestas que las herramientas le devuelven al modelo.
# Cada respuesta tiene un estado (ver ESTADO_... en configuracion.py) y los datos encontrados.
from ... import configuracion
from . import materias, superposiciones

def buscarHorarios(oferta, materia, comision):
    horarios = horariosDeMateria(oferta, materia)
    materiasEncontradas = materias.valoresDistintos(horarios, configuracion.POSICION_MATERIA)

    if len(horarios) == 0:
        return armarRespuesta(configuracion.ESTADO_MATERIA_NO_ENCONTRADA, [])

    if len(materiasEncontradas) > 1:
        return armarRespuesta(configuracion.ESTADO_VARIAS_MATERIAS, materiasEncontradas)

    return elegirComision(horarios, comision)


def elegirComision(horarios, comision):
    comisiones = materias.valoresDistintos(horarios, configuracion.POSICION_COMISION)

    if comision == "" and len(comisiones) > 1:
        return armarRespuesta(configuracion.ESTADO_FALTA_COMISION, comisiones)

    if comision == "":
        return armarRespuesta(configuracion.ESTADO_OK, horarios)

    horariosDeComision = materias.filtrarPorComision(horarios, comision)

    if len(horariosDeComision) == 0:
        return armarRespuesta(configuracion.ESTADO_COMISION_NO_ENCONTRADA, comisiones)

    return armarRespuesta(configuracion.ESTADO_OK, horariosDeComision)


def horariosDeMateria(oferta, materia):
    # Si el nombre coincide exacto, se queda solo con esa materia: "Programación I" no trae "Programación II".
    horarios = materias.buscarMateria(oferta, materia)
    horariosExactos = materias.filtrarMateriaExacta(horarios, materia)

    if len(horariosExactos) > 0:
        return horariosExactos

    return horarios


def buscarSuperposicion(oferta, materiaA, comisionA, materiaB, comisionB):
    respuestaA = buscarHorarios(oferta, materiaA, comisionA)
    respuestaB = buscarHorarios(oferta, materiaB, comisionB)

    if estadoDe(respuestaA) != configuracion.ESTADO_OK:
        return respuestaA

    if estadoDe(respuestaB) != configuracion.ESTADO_OK:
        return respuestaB

    pares = superposiciones.buscarSuperposiciones(datosDe(respuestaA), datosDe(respuestaB))

    return armarRespuesta(configuracion.ESTADO_OK, pares)


# La respuesta es un diccionario porque ADK se la pasa así al modelo.
# Estas tres funciones son las únicas que lo tocan.
def armarRespuesta(estado, datos):
    return {"estado": estado, "datos": datos}


def estadoDe(respuesta):
    return respuesta["estado"]


def datosDe(respuesta):
    return respuesta["datos"]
