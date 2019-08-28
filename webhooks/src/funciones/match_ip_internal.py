#!/usr/bin/python3

from parametros import *
from netaddr import IPNetwork, IPAddress
import urllib.request 

#recibe una ip y chequea si es interna en PSI UNC consultando la base wiki

def match_ip_internal(data):

    data = json.loads(request.data.decode('utf-8'))
    artifacts=data['object']['artifacts']

    source_ip = 0
    destination_ip = 0
    source_ip_internal = 0
    destination_ip_internal = 0

    # para cada objeto de la lista artifacts filtro por la
    # linea que tiene destination_ip como ip.
    for element in artifacts:
        if element["dataType"] == "source_ip":
            source_ip = element["data"]
            # print ("IP origen: " + source_ip)
        if element["dataType"] == "destination_ip":
            destination_ip = element["data"]
            # print ("IP destino: " + destination_ip)


#Se obtienen las ip por octetos!

    source_ip_internal_octectos =  source_ip.split('.') #array de octetos separados con punto!
    source_ip_internal_tres_octectos =  source_ip_internal_octectos[0] + "." + source_ip_internal_octectos[1] + "." +  source_ip_internal_octectos[2]

    destination_ip_internal_octectos =  destination_ip.split('.') #array de octetos separados con punto!
    destination_ip_internal_tres_octectos =  destination_ip_internal_octectos[0] + "." + destination_ip_internal_octectos[1] + "." +  destination_ip_internal_octectos[2]


    # print("source_ip_internal_tres_octectos:" + source_ip_internal_tres_octectos)
    # print("destination_ip_internal_tres_octectos:" + destination_ip_internal_tres_octectos)

    #Obtengo las IP que coinciden con los tres octetos de la wiki para ip
    #activos PSI definido en parametros.py

    url_source = activosPSI + source_ip_internal_tres_octectos
    url_destination = activosPSI + destination_ip_internal_tres_octectos

    response_source = urllib.request.urlopen(url_source)
    response_destination = urllib.request.urlopen(url_destination)

    data_source = response_source.read()
    values_source = json.loads(data_source)

    data_destination = response_destination.read()
    values_destination  = json.loads(data_destination)
 
#Busco si hay matcheo con 3 octetos recorriendo el json (tiene en cuenta la mascara)
    for dato in values_source:
    #    print("Json:" + dato['name'])
        if IPAddress(source_ip) in IPNetwork(dato['name']): #coinciden ip guardo IP en array
                # print(dato['name'])
                #print("La source_ip es ip es interna!")
                source_ip_internal = 1
                break;

    # Busco si hay matcheo con 3 octetos recorriendo el json (tiene en cuenta la mascara)
    for dato in values_destination:
        #    print("Json:" + dato['name'])
        if IPAddress(destination_ip) in IPNetwork(dato['name']):  # coinciden ip guardo IP en array
            #print(dato['name'])
            #print("La destination_ip es ip es interna!")
            destination_ip_internal = 1
            break;


    if (destination_ip_internal != 0  or source_ip_internal != 0):
        return 1
    else:
        return 0
