# Ejercicio de un metodo que retorna una lista de numeros pares
import random


numeros = []
for n in range(0,100):
    numeros.append(random.randint(1,100))



def pares(listanumeros):
    return [num for num in listanumeros if num%2==0]

print(numeros)
print(f'Los números pares de la lista son: {pares(numeros)}')