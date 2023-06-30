def primera_letra_repetida(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacio = texto_minuscula.replace(" ","")
    lista_letras = []
    for letra in texto_sin_espacio:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)

    return None

print(primera_letra_repetida("Hola"))
print(primera_letra_repetida("hola mundo estamos juntos"))


