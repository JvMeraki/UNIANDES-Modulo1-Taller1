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