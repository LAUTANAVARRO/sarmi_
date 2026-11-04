from ..utilidades.textos import contiene, normalizar, extraerNumero
from ..utilidades.listas import esta
from ...configuracion import POSICION_MATERIA, POSICION_COMISION

def valoresDistintos(horarios, posicion):
    """Recibe una lista de horarios y una posición (ver POSICION_... en configuracion.py).
    Junta el dato que está en esa posición en cada horario, sin repetir.
    Devuelve la lista de esos valores, en el orden en que aparecen.
    Ejemplo: con los horarios de Introducción a la Programación y POSICION_COMISION,
    devuelve ["COM-01", "COM-02", "COM-03", ...]."""

    distintos = []
    for horario in horarios:
        valor = horario[posicion]
        if valor not in distintos:
            distintos.append(valor)
    return distintos
    


def buscarMateria(oferta, nombre):
    """Recibe la oferta y el nombre de una materia, o una parte (por ejemplo "programacion").
    Busca los horarios cuya materia contiene ese nombre, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: buscarMateria(oferta, "programacion") devuelve los horarios de Introducción a la
    Programación, Programación I, Programación II y otras."""

    resultados = []
    for horario in oferta:
        materia = horario[POSICION_MATERIA]
        if contiene(materia, nombre):
            resultados.append(horario)
    return resultados


def filtrarMateriaExacta(horarios, nombre):
    """Recibe una lista de horarios y el nombre de una materia.
    Se queda con los horarios cuya materia se llama exactamente así, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: si están los horarios de Programación I y de Programación II, con "programación i"
    devuelve solo los de Programación I."""

    resultados = []
    nombre_norm = normalizar(nombre)
    for horario in horarios:
        materia_norm = normalizar(horario[POSICION_MATERIA])
        if materia_norm == nombre_norm:
            resultados.append(horario)
    return resultados

    

def filtrarPorComision(horarios, comision):
    """Recibe una lista de horarios y una comisión, escrita como sea ("7", "07", "COM-07" o "comisión 7").
    Se queda con los horarios de esa comisión, comparando solo el número.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: con los horarios de Introducción a la Programación y "7", devuelve los dos horarios
    de la COM-07: el del viernes y el virtual."""
    
    num_buscado = extraerNumero(str(comision))
    resultados = []
    for horario in horarios:
        comision_actual = horario[POSICION_COMISION]
        num_actual = extraerNumero(comision_actual)
    
        if num_buscado != -1 and num_buscado == num_actual:
            resultados.append(horario)
        elif normalizar(str(comision)) == normalizar(comision_actual):
            resultados.append(horario)
    return resultados
