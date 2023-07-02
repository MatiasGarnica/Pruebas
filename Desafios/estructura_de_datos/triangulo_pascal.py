def triangulo_pascal(filas):

    lista_anidada = []
    for i in range(filas):
        sublista = []
        for posicion in range(i+1):
            if posicion == 0 or posicion == i:
                sublista.append(1)
            else:
                print(posicion)
                valor = lista_anidada[i-1][posicion-1] + lista_anidada[i-1][posicion]
                sublista.append(valor)
        print(lista_anidada)
        lista_anidada.append(sublista)

    return lista_anidada
        



print(triangulo_pascal(5))