import json
archivo = open('./s2/SINALOA/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON

counter = 0

def retrieve(x):
    try:
        return x['ramo']['valor']
    except (KeyError, TypeError):
        return False
for x in datos:
    valor = retrieve(x)
    print(valor)
    counter += 1
print(counter)