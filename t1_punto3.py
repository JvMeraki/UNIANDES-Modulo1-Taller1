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