def horarios_convertidos(hora):
    hora_lista = hora.split(":")
    if hora[-2:].lower() == "pm":
        if hora_lista[0] != "12":
            hora_lista[0] = str(int(hora_lista[0])+12)
    else:
        if hora_lista[0] == "12":
            hora_lista[0] = "00"
    hora_convertida = ":".join(hora_lista)
    return hora_convertida[:-2]

print(horarios_convertidos("04:00AM"))
print(horarios_convertidos("04:59pm"))
print(horarios_convertidos("10:00:00PM"))




