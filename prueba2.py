
def calcular(numero):
    return numero**2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = []

for num in lista_num:
    cuadrado = calcular(num)
    if cuadrado %2 == 0:
        lista_pares.append(cuadrado)
"""         print(f"El cuadrado de {num} es {cuadrado}, es un numero par")
    else:
        print(f"El cuadrado de {num} es {cuadrado}, es un numero impar") """

print(lista_pares)


pares_comprehension = [cuadrado for num in lista_num if (cuadrado := calcular(num)) % 2 == 0]

print(pares_comprehension)
