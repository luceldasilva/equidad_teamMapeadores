import json
archivo = open('./s2/SINALOA/data-0000000001.json',encoding="utf8") # 1 . Se ubica el archivo JSON para abrirlo. 

datos = json.load(archivo) #2. Se carga el archivo JSON dentro del ecosistema de analisis de JSON

counter = 0
listaDependencias = [] #se crea una lista de dependencias. 

def retrieve(x): #Se busca ahora que se regrese el valor de ramo por cada registro.
    try:
        return x['ramo']['valor'] #retorna el valor del ramo 
    except (KeyError, TypeError):
        return False
for x in datos: #En cada registro
    valor = retrieve(x) #se ejecuta esta función que recupera el valor del ramo dependencia 
    listaDependencias.append(valor) #se inserta una dependencia a la lista

listaDependencias = list(set(listaDependencias)) #se quitan los valores duplicados
print(listaDependencias) #imprime la lista de dependencias aparte. son 8

# Se procede a contar el total de mujeres por dependencia. 

for ramo in listaDependencias:
    
    def filtro(x):
        #print(ramo)
        if(x['genero']['valor'] == 'FEMENINO' and x['ramo']['valor'] == ramo):
          #  print(ramo)
            return True
        else:
            return False
     #en filter solo regresan los que dan true en la funcion    
    resultado = list(filter(filtro,datos)) #se busca filtrar por genero que será siempre 'FEMENINO' y por la dependencia en turno 
    print(resultado)
  #  print(x) , vimos que si aparece cada rama dependencia registrado  
#print(resultado)
#print(resultado)