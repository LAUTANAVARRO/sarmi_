

def horaAMinutos(hora):
    """Recibe una hora escrita como "HH:MM".
    Calcula cuántos minutos pasaron desde las 00:00.
    Devuelve esa cantidad de minutos.
    Ejemplo: horaAMinutos("18:30") devuelve 1110."""

    partes = hora.split(":")
    horas_enteras = int(partes[0])
    minutos_enteros = int(partes[1])
    
    total_minutos = (horas_enteras * 60) + minutos_enteros

    return total_minutos