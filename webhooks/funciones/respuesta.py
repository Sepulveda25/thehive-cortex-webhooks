#!/usr/bin/python3

from parametros import *
from netaddr import IPNetwork, IPAddress
import urllib.request 
#from web_application_attack import *

def respuesta():	
#parseo de la alerta:
#obtengo campo artifacts:
    
    print("Programa de respuesta automatica")
    data = json.loads(request.data.decode('utf-8'))
    artifacts=data['object']['artifacts']
 
    #en el campo description tenemos category!

    description = data['object']['description']
    print ("description: " + description)


    source_ip = 0
    destination_ip = 0
    source_ip_internal = 0	
    destination_ip_internal = 0

#para cada objeto de la lista artifacts filtro por la
#linea que tiene destination_ip como ip.
    for element in artifacts:
        if element["dataType"]=="source_ip":
            source_ip = element["data"]  	   
            print ("IP origen: " + source_ip)
        if element["dataType"]=="destination_ip":
            destination_ip = element["data"]  	   
            print ("IP destino: " + destination_ip)

#Se obtienen las ip por octetos!
    source_ip_octetos = source_ip.split('.') #array de octetos separados con punto!
    destination_ip_octetos = destination_ip.split('.')

    source_ip_tresOctetos =  source_ip_octetos[0] + "." + source_ip_octetos[1] + "." +  source_ip_octetos[2]
    destination_ip_tresOctetos = destination_ip_octetos[0] + "." + destination_ip_octetos[1] + "." + destination_ip_octetos[2]
#    print("source_ip_tresOctetos:" + source_ip_tresOctetos)
#    print("destination_ip_tresOctetos:" + destination_ip_tresOctetos)

#Obtengo las IP que coinciden con los tres octetos de la wiki para source_ip
#activos PSI definido en parametros.py 

    url = activosPSI + source_ip_tresOctetos
    response = urllib.request.urlopen(url)
    data = response.read()
    values = json.loads(data)

#Busco si hay matcheo con 3 octetos recorriendo el json (tiene en cuenta la mascara)
    for dato in values:
#        print("Json:" + dato['name'])
        if IPAddress(source_ip) in IPNetwork(dato['name']): #coinciden source_ip guardo IP en array
#                print(source_ip)
#                print(dato['name'])
                print("La red es source_ip es interna!")
                source_ip_internal = 1
                break;

#Obtengo las IP que coinciden con los tres octetos de la wiki para destination_ip
#activos PSI definido en parametros.py 

    url = activosPSI + destination_ip_tresOctetos
    response = urllib.request.urlopen(url)
    data = response.read()
    values = json.loads(data)

#Busco si hay matcheo con 3 octetos recorriendo el json (tiene en cuenta la mascara)
    for dato in values:
#        print("Json:" + dato['name'])
        if IPAddress(destination_ip) in IPNetwork(dato['name']): #coinciden source_ip guardo IP en array
#                print(destination_ip)
#                print(dato['name'])
                print("La red es destination_ip es interna!")
                destination_ip_internal = 1
                break;


#busco en el campo description si coincide con la clasificacion
    if (description.find("Web Application Attack") > 0):
        print ("Encontre clasificacion: Web Application Attack")
	#web_application_attack()






