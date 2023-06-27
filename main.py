
def calcular(numero):
    return numero**2

def es_par(numero):
    return numero % 2 == 0

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = [calcular(num) for num in lista_num]
print(lista_cuadrados)
