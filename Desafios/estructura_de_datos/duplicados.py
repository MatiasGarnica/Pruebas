def elementos_duplicados(lista):

    lista_duplicados = []
    elementos_lista = []
    for elemento in lista:
        if elemento in elementos_lista:
            lista_duplicados.append(elemento)
            #lista_individual = list(set(lista_duplicados))
        #if elemento not in elementos_lista:
        else:
            elementos_lista.append(elemento)
            

    return lista_duplicados

print(elementos_duplicados(["casa", "gato", "perro", "conejo", "casa", "gato", "gato", "pala"]))