# Punto 4 | Clasificando Palabras
def clasificacion(palabras:list) -> dict:
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario
print(clasificacion(["Muchos","Muchos", "años", "después", "frente", "al"]))
print(clasificacion(["Hola", "Mundo", "Python", "Clase", "Programación", "Universidad", "Andes"]))