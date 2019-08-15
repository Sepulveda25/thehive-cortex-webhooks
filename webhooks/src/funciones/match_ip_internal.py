#!/usr/bin/python3

from parametros import *
from netaddr import IPNetwork, IPAddress
import urllib.request 

#recibe una ip y chequea si es interna en PSI UNC consultando la base wiki

def match_ip_internal(ip): #COMPLEATRRRRRRR

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
            #            print ("IP origen: " + source_ip)
        if element["dataType"] == "destination_ip":
            destination_ip = element["data"]
            #            print ("IP destino: " + destination_ip)
	
    ip_internal = 0
#Se obtienen las ip por octetos!
    ip_octetos = ip.split('.') #array de octetos separados con punto!
    ip_tresOctetos =  ip_octetos[0] + "." + ip_octetos[1] + "." +  ip_octetos[2]

#    print("ip_tresOctetos:" + ip_tresOctetos)

#Obtengo las IP que coinciden con los tres octetos de la wiki para ip
#activos PSI definido en parametros.py 

    url = activosPSI + ip_tresOctetos
    response = urllib.request.urlopen(url)
    data = response.read()
    values = json.loads(data)
 
#Busco si hay matcheo con 3 octetos recorriendo el json (tiene en cuenta la mascara)
    for dato in values:
#        print("Json:" + dato['name'])
        if IPAddress(ip) in IPNetwork(dato['name']): #coinciden ip guardo IP en array
 #               print(ip)
 #               print(dato['name'])
 #               print("La red es ip es interna!")
                ip_internal = 1
                break;

    if (ip_internal != 0):
        return 1
    else:
        return 0
