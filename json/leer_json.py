import json

with open("persona.json", "r") as archiv_json:
    datos_json = json.load(archiv_json)

print(datos_json["nombre"])


