#!/usr/bin/python3

from parametros import *
from web_application_attack import *

def web_application_attack():	
#parseo de la alerta:
#obtengo campo artifacts:
    
    print("Soy el programa de respuesta!")
    data = json.loads(request.data.decode('utf-8'))
    artifacts=data['object']['artifacts']
 
    #en el campo description tenemos category!

    description = data['object']['description']
    print ("description: " + description)


    source_ip = 0
    destination_ip = 0



#para cada objeto de la lista artifacts filtro por la
#linea que tiene destination_ip como ip.
    for element in artifacts:
        if element["dataType"]=="source_ip":
            source_ip = element["data"]  	   
            #print ("IP origen: " + source_ip)
        if element["dataType"]=="destination_ip":
            destination_ip = element["data"]  	   
            #print ("IP destino: " + destination_ip)

#busco si hay ip externa o interna
    octetos_source_ip = source_ip.split('.')
    octetos_destination_ip = destination_ip.split('.')
    dosOctetos = octetos[0] + "." + octetos[1]
    tresOctetos = dosOctetos + "." + octetos[2]

#busco en el campo description si coincide con la clasificacion
    if (description.find("Web Application Attack") > 0):
        print ("Si encontre clasificacion")
	web_application_attack()




