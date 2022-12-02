import json

archivo = open('./s2/SINALOA/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
counter = 0
def filtro(x):  #3. Se consulta por Institución (ramo) y se filtra para obtener solo a las mujeres
    try:
        return x['genero']['valor'] == 'FEMENINO' and x['ramo']['valor'] == 'INSTITUTO MUNICIPAL DE PLANEACIÓN DE MAZATLÁN'
    except (KeyError, TypeError):
        return False

# resultado=list(filter(filtro, datos))
# print(resultado)
resultado = filter(filtro, datos)
for x in datos:
  counter += 1

print(counter)

archivo.close()