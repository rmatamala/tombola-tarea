import random
import csv
from  config import conf 

lista_concursantes = []
lista_premios = []
lista_premio_ganadores = []

def getData():
    archivo1 = open(conf["CONCURSANTES_PATH"], "r")
    reader1 = csv.reader(archivo1)
    archivo2 = open(conf["PREMIOS_PATH"], "r")
    reader2 = csv.reader(archivo2)

    for linea in reader1:
        lista_concursantes.append(linea[0])

    for linea in reader2:
        lista_premios.append(linea[0])


try:

    # Se llama a funcion que obtiene datos para concurso
    getData()
 
    pg = {}
    sortear=True

    for premio in lista_premios:
        # print(premio)
        while sortear:

            # Se obtiene numero de concursante ganador
            sorteo = random.randint(0, len(lista_concursantes)-1)           
            concursante = lista_concursantes[sorteo]

            # Validar si tiene mas de dos premios
            if concursante in pg:
                listaux=[]
                listaux=pg[concursante]
                if len(listaux) < 2:
                    listaux.append(premio)
                    pg[concursante] = listaux
                    sortear=False
                else:
                    #El concursante ya tiene dos premios, volver a sortear el premio
                    print(concursante," Ya tiene mas de dos premios se vuelve a sortear el premio :",premio)
                    sortear=True

            else:
                pg[concursante] = [premio]
                sortear=False

        #Este va fuera del while
        sortear=True

    print(pg)

    # Salida
    with open(conf["RESULTADOS_PATH"], 'w', newline='') as f:
        writer = csv.writer(f)
  
        for key in pg:
            dato="El Concursante : "+ key + " gano el premio: "+str(pg[key])
            writer.writerow([dato])
       

except Exception as err:
    print("Exception",err)



