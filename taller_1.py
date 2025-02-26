import Taller1.t1_punto1 as p1
from Taller1.t1_punto2 import *

print("\n","----"*20,"\n")
# Punto 1 | El IMC
def imc(peso:int, altura:float) -> float:
    if peso < 0 or altura < 0:
        return "Los valores ingresados no son válidos"
    else:
        resultado =  peso / altura**2
        decimales = 2
        rounded_result = round(resultado, decimales)
    return rounded_result
print(imc(70, 1.75))

print("\n","----"*20,"\n")



# Punto 2 | Años Bisiestos
def bisiesto(año:int) -> str:
    if (año%4 == 0 and año%100 != 0) or año%400 == 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")
print(bisiesto(2024))
#1900, 2000, 2100, 2200, 2300, 2500, 2600, 2700, 2800, 2900, 3000

print("\n","----"*20,"\n")

# Punto 3 | ¿Usted me divida?
def divisible(num1: int, num2: int) -> list:
    lista = []
    if not (1 <= num1 <= 100 and 1 <= num2 <= 100):
        print("Los números no están entre 1 y 100")    
        return lista
    else:
        print("Los números están entre 1 y 100")
        for i in range (1,101):
            if i%num1 == 0 and i%num2 == 0:
                lista.append(i)
        return lista
print(divisible(10, 3))
    
print("\n","----"*20,"\n")
    
# Punto 4 | Clasificando Palabras
def clasificacion(palabras:list) -> dict:
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario
print(clasificacion(["Muchos","Muchos", "años", "después", "frente", "al"]))
print(clasificacion(["Hola", "Mundo", "Python", "Clase", "Programación", "Universidad", "Andes"]))

print("\n","----"*20,"\n")