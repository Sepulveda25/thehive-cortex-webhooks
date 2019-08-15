#!/usr/bin/python3

from parametros import *
from match_ip_internal import *
from web_application_attack import *



def respuesta_automatica():
#parseo de la alerta:
#obtengo campo artifacts:
    
    print("Programa de respuesta automatica")
    data = json.loads(request.data.decode('utf-8'))
    artifacts=data['object']['artifacts']
 
    #en el campo description tenemos category!

    description = data['object']['description']
#  print ("description: " + description)

    source_ip = 0
    destination_ip = 0
    source_ip_internal = 0	
    destination_ip_internal = 0

#para cada objeto de la lista artifacts filtro por la
#linea que tiene destination_ip como ip.
    for element in artifacts:
        if element["dataType"]=="source_ip":
            source_ip = element["data"]  	   
#            print ("IP origen: " + source_ip)
        if element["dataType"]=="destination_ip":
            destination_ip = element["data"]  	   
#            print ("IP destino: " + destination_ip)

#busco en el campo description si coincide con la clasificacion
    if (description.find("Web Application Attack") > 0):
   #     if (match_ip_internal(source_ip) == 1):
   #             source_ip_internal = 1;
   #             print ("IP origen es interna")
   #     if ( match_ip_internal(destination_ip) == 1):
   #             destination_ip_internal = 1;
   #             print ("IP destino es interna")
   #     if(source_ip_internal == 1 or destination_ip_internal == 1):
        web_application_attack(data)








