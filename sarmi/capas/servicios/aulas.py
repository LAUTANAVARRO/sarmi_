
from ..utilidades.textos import normalizar
from ..utilidades.horas import horaAMinutos
from ..utilidades.listas import copiarLista
from ...configuracion import POSICION_AULA, POSICION_DIA, POSICION_HORA_INICIO

def horariosEnAula(oferta, aula, dia):
    """Recibe la oferta, un aula (por ejemplo "7118") y un día (por ejemplo "viernes").
    Busca los horarios que se dictan en esa aula ese día, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: horariosEnAula(oferta, "7118", "viernes") devuelve los horarios de Análisis
    Numérico y de Introducción a la Programación."""

    resultados = []
    aula_buscada = normalizar(str(aula))
    dia_buscado = normalizar(dia)
    
    for horario in oferta:
        aula_actual = normalizar(str(horario[POSICION_AULA]))
        dia_actual = normalizar(horario[POSICION_DIA])
        
        # Busca el número de aula (ej: "7118" en "LABO COM 7118")
        if (aula_buscada in aula_actual) and (dia_buscado == dia_actual):
            resultados.append(horario)
    return resultados


def ordenarPorHora(horarios):
    """Recibe una lista de horarios.
    Arma una copia ordenada por hora de inicio, de la más temprana a la más tarde, con el método
    de inserción (sin usar sorted). La lista que recibe no cambia.
    Devuelve la lista ordenada.
    Ejemplo: con un horario que empieza a las 18:00 y otro a las 13:00, devuelve primero el de las 13:00."""
    
    lista_ordenada = []
    for horario in horarios:
        lista_ordenada.append(horario)
        
    n = len(lista_ordenada)
    for i in range(1, n):
        clave = lista_ordenada[i]
        minutos_clave = horaAMinutos(clave[POSICION_HORA_INICIO])
        j = i - 1
        while j >= 0 and horaAMinutos(lista_ordenada[j][POSICION_HORA_INICIO]) > minutos_clave:
            lista_ordenada[j + 1] = lista_ordenada[j]
            j -= 1
        lista_ordenada[j + 1] = clave
        
    return lista_ordenada
