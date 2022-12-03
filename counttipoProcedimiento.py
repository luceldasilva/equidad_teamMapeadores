import json

archivo = open('./s2/SINALOA/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON
counter = 0
def filtro(x):  #3. Se consulta por Institución (ramo) y se filtra para obtener solo a las mujeres
    try:
        return x['genero']['valor'] == 'FEMENINO' and x['tipoProcedimiento'][0]['valor'] == 'CONTRATACIONES PÚBLICAS'
    except (KeyError, TypeError):
        return False

# resultado=list(filter(filtro, datos))
# print(resultado)
resultado = filter(filtro, datos)
for x in resultado:
  counter += 1 

print(counter) #esto es el numero que se muestra de mujeres en tal campo 

archivo.close()