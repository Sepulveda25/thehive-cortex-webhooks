#!/usr/bin/python3

from parametros import *

def alert_new():	
#parseo de la alerta:
#obtengo campo artifacts:
    
    print("Nueva Alerta!")
    data = json.loads(request.data.decode('utf-8'))
    artifacts=data['object']['artifacts']

    source_ip = 0
    destination_ip = 0
    source_port = 0
    destination_port = 0

#para cada objeto de la lista artifacts filtro por la
#linea que tiene destination_ip como ip.
    for element in artifacts:
        if element["dataType"]=="source_ip":
            source_ip = element["data"]  	   
            print ("IP origen: " + source_ip)
        if element["dataType"]=="destination_ip":
            destination_ip = element["data"]  	   
            print ("IP destino: " + destination_ip)
        if element["dataType"]=="source_port":
            source_port = element["data"]  	   
            print ("Puerto origen: " + source_port)
        if element["dataType"]=="destination_port":
            destination_port = element["data"]  	   
            print ("Puerto destino: " + destination_port)


    payload = {"attachments": [
        {
            "fallback": "Alert incoming",
            "pretext": "Respuesta?",
            "author_name": "Updated by " + (str(data['object']['source'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been updated" + "source: " + (str(data['object']['source'])) + "Ip:" + str(artifacts),
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)	
    "Response: " + str(r.status_code) + "," + str(r.reason)

#envia a SLACK y ahora crea un caso automaticamente.

