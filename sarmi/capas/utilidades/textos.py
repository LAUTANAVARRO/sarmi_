

def normalizar(texto):
    """Recibe un texto.
    Lo pasa a minúsculas y le saca las tildes (ver LETRAS_CON_TILDE en configuracion.py).
    Devuelve el texto nuevo.
    Ejemplo: normalizar("Introducción a la PROGRAMACIÓN") devuelve "introduccion a la programacion"."""
    
    texto = texto.lower()
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
        'ü': 'u', 'Ü': 'u'
        }  

    for letra_con_tilde, letra_sin_tilde in reemplazos.items():
        texto = texto.replace(letra_con_tilde, letra_sin_tilde)

    return texto


def contiene(texto, buscado):
    """Recibe dos textos: texto y buscado.
    Se fija si buscado aparece en alguna parte de texto.
    Devuelve True si aparece y False si no.
    Ejemplo: contiene("introduccion a la programacion", "program") devuelve True."""

    texto = normalizar(texto)
    buscado = normalizar(buscado)
    

    return buscado in texto


def extraerNumero(texto):
    """Recibe un texto.
    Junta los dígitos que aparecen en el texto y los convierte en número.
    Devuelve ese número, o -1 si el texto no tiene dígitos.
    Ejemplo: extraerNumero("COM-07") devuelve 7."""
    digitos = ""
    for caracter in texto:
            if caracter.isdigit():
                 digitos += caracter
    if digitos == "":
         return -1
    else:
         return int(digitos)
