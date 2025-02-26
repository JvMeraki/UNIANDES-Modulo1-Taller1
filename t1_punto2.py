# Punto 2 | Años Bisiestos
def bisiesto(año:int) -> str:
    if (año%4 == 0 and año%100 != 0) or año%400 == 0:
        return f"El {año} es bisiesto"
    else:
        return f"El {año} no es bisiesto"
print(bisiesto(2024))