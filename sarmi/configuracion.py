import os

# Datos
CARPETA_DEL_AGENTE = os.path.dirname(__file__)
RUTA_OFERTA = os.path.join(CARPETA_DEL_AGENTE, "datos", "oferta.csv")
PRIMERA_FILA_CON_DATOS = 1
PERIODO = "segundo semestre de 2026"

# Posición de cada dato dentro de un horario
POSICION_MATERIA = 1
POSICION_COMISION = 2
POSICION_DIA = 5
POSICION_HORA_INICIO = 6
POSICION_HORA_FIN = 7
POSICION_AULA = 8

DIA_VIRTUAL = "VT ASINC"

# Cada letra de LETRAS_CON_TILDE se reemplaza por la de la misma posición en LETRAS_SIN_TILDE
LETRAS_CON_TILDE = "áéíóúü"
LETRAS_SIN_TILDE = "aeiouu"

# Cada turno es [nombre, hora de inicio, hora de fin]
TURNOS = [
    ["mañana", "08:00", "12:59"],
    ["tarde", "13:00", "17:59"],
    ["noche", "18:00", "23:59"],
]

# Estados que devuelven las herramientas (el modelo los lee tal cual)
ESTADO_OK = "ok"
ESTADO_VARIAS_MATERIAS = "variasMaterias"
ESTADO_FALTA_COMISION = "faltaComision"
ESTADO_MATERIA_NO_ENCONTRADA = "materiaNoEncontrada"
ESTADO_COMISION_NO_ENCONTRADA = "comisionNoEncontrada"

# Controles
PALABRAS_NO_PERMITIDAS = []
MENSAJE_PREGUNTA_NO_PERMITIDA = "Soy SarmIA y solo puedo responder consultas sobre materias, horarios y aulas de la UNGS."

# Agente
MODELO = os.environ.get("MODELO_GEMINI", "gemini-3.5-flash-lite")
NOMBRE_DEL_AGENTE = "sarmi"
DESCRIPCION_DEL_AGENTE = "SarmIA, el agente de la UNGS: responde consultas sobre materias, comisiones, horarios y aulas."
SALUDO = """¡Hola! Soy SarmIA, el agente de la UNGS. Te ayudo a encontrar en qué día, horario y aula \
se cursa cada materia, qué se dicta en un aula y si dos comisiones se superponen. ¿Qué querés consultar?"""
INSTRUCCIONES_DEL_AGENTE = """
Te llamás SarmIA y sos el agente conversacional de la Universidad Nacional de General Sarmiento (UNGS).
Cuando el usuario te salude o te pregunte quién sos, presentate con este saludo: """ + SALUDO + """
Respondés consultas sobre materias, comisiones, días, horarios y aulas del """ + PERIODO + """.
Usá siempre las herramientas. Nunca inventes datos.
Cada horario es una lista: [código, materia, comisión, fecha de inicio, fecha de fin, día, hora de inicio,
hora de fin, aula, edificio, tipo de cursada, instituto, instancia, compartida con].
Cuando la herramienta responde con el estado:
- """ + ESTADO_VARIAS_MATERIAS + """: mostrá los nombres y preguntá a cuál se refiere.
- """ + ESTADO_FALTA_COMISION + """: mostrá las comisiones y preguntá en cuál está.
- """ + ESTADO_MATERIA_NO_ENCONTRADA + """ o """ + ESTADO_COMISION_NO_ENCONTRADA + """: decíselo al usuario.
Los horarios con día """ + DIA_VIRTUAL + """ son virtuales asincrónicos: no tienen aula ni hora.
Respondé en español rioplatense, en pocas líneas.
Si el usuario pregunta qué comisiones hay de una materia, mostrale todas las comisiones que devuelve la herramienta,
numeradas. No respondas solo con la cantidad o el rango ni preguntes si quiere que se las enumeres.
Cuando haya varias materias o comisiones, mostrá las opciones numeradas desde el 1 y preguntá cuál elige el usuario. Si
responde solo con un número, interpretalo como la opción correspondiente de la lista que acabás de mostrar y continuá la
consulta usando esa opción. Si el número no corresponde a ninguna opción, volvé a mostrar la lista. 
"""
