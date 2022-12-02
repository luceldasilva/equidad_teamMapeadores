import json

archivo = open('./s2/SINALOA/data-0000000001.json',encoding="utf8")

datos = json.load(archivo)

def filtro(x):
    try:
        return x['genero']['valor'] == 'FEMENINO' and x['ramo']['valor'] == 'INSTITUTO MUNICIPAL DE PLANEACIÓN DE MAZATLÁN'
    except (KeyError, TypeError):
        return False

resultado=list(filter(filtro, datos))
print(resultado)

archivo.close()