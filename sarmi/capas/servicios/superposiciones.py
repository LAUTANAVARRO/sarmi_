from ...configuracion import ( DIA_VIRTUAL, POSICION_DIA, POSICION_HORA_INICIO, POSICION_HORA_FIN)
from ..utilidades.horas import horaAMinutos


def seSuperponen(horarioA, horarioB):
    """Recibe dos horarios.
    Se fija si los dos son presenciales, son el mismo día y sus horas se cruzan.
    Si uno termina justo cuando empieza el otro (de 14 a 18 y de 18 a 22), no se superponen.
    Devuelve True si se superponen y False si no.
    Ejemplo: un viernes de 18:00 a 22:00 y un viernes de 20:00 a 22:00 se superponen: devuelve True."""

    dia_a = horarioA[POSICION_DIA]
    dia_b = horarioB[POSICION_DIA]

    # Verifica los horarios no sean virtuales
    if dia_a == DIA_VIRTUAL or dia_b == DIA_VIRTUAL:
        return False

    # Verifica que ambos horarios sean diferentes
    if dia_a != dia_b:
        return False

    # Verifica que los horarios sean virtuales, si lo son no se superponen
    if not horarioA[POSICION_HORA_INICIO] or not horarioA[POSICION_HORA_FIN]:
        return False
    if not horarioB[POSICION_HORA_INICIO] or not horarioB[POSICION_HORA_FIN]:
        return False

    # Guardo las horas de inicio y fin de los horarios para comparalos
    inicio_a = horaAMinutos(horarioA[POSICION_HORA_INICIO])
    fin_a = horaAMinutos(horarioA[POSICION_HORA_FIN])

    inicio_b = horaAMinutos(horarioB[POSICION_HORA_INICIO])
    fin_b = horaAMinutos(horarioB[POSICION_HORA_FIN])

    # verifica si los horarios se superponen y devuelve la respuesta
    return inicio_a < fin_b and inicio_b < fin_a


def buscarSuperposiciones(horariosA, horariosB):
    """Recibe dos listas de horarios (por ejemplo, los de dos comisiones).
    Compara cada horario de la primera lista con cada horario de la segunda.
    Devuelve una lista de pares [horarioA, horarioB] que se superponen, o una lista vacía si no hay ninguno.
    Ejemplo: con [viernesDe18a22] y [viernesDe20a22, lunesDe18a22] devuelve [[viernesDe18a22, viernesDe20a22]]."""

    pares = []

    # Recorre los horarios y los compara para ver si se superponen
    for horario_a in horariosA:
        for horario_b in horariosB:
            if seSuperponen(horario_a, horario_b):
                pares.append([horario_a,horario_b])
    
    return pares
