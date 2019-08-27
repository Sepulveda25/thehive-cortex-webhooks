import json
import os

from parametros import *


#transformo el JSON de entrada a TheHive a un JSON de entrada a Cortex

def hive2cortex(imput_json):

    json_aux = {
        "data": {
            "_id": imput_json['object']["severity"],
            "_parent": imput_json['object']["_parent"], #Distinto viene "None" y pone null
            "_routing": imput_json['object']["_routing"],
            "_type": imput_json['object']["_type"],
            "_version": imput_json['object']["_version"],
            "artifacts": imput_json['object']["artifacts"],  #Distinto viene  "message": "None" y pone "message": null
            "caseTemplate": imput_json['object']["caseTemplate"], #Distinto viene "None" y pone null
            "createdAt": imput_json['object']["createdAt"],
            "createdBy": imput_json['object']["createdAt"],
            "customFields": imput_json['object']["customFields"],
            "date":  imput_json['object']["date"],
            "description": imput_json['object']["description"],
            "follow":  imput_json['object']["follow"],  #Distinto viene "True" y pone true
            "id": imput_json['object']["id"],
            "lastSyncDate": imput_json['object']["lastSyncDate"],
            "severity": imput_json['object']["severity"],
            "source": imput_json['object']["source"],
            "sourceRef": imput_json['object']["sourceRef"],
            "status": imput_json['object']["status"],
            "tags": imput_json['object']["tags"],
            "title":imput_json['object']["title"],
            "tlp": imput_json['object']["tlp"],
            "type": imput_json['object']["type"]
        },
        "dataType": "thehive:alert", #NO SE SACA DE LA ALERTA
        "label": "[" + imput_json['object']["source"] + ":" + imput_json['object']["sourceRef"] + "] " + imput_json['object']["title"],
        "tlp": "2" + " - ???", #NO SE SACA DE LA ALERTA
        "pap": "2" + " - ???", #NO SE SACA DE LA ALERTA
        "message": "",
        "parameters": {
            "user": "eco - GET user FROM THEHIVE" #NO SE SACA DE LA ALERTA
        }
    }


    #Cuando se convierte a formato json los campos con "None" se transforman en null y "True" en true
    #Pero esto no es necesario para el programa Responder
    #json2cortex = json.dumps(json_aux)

#    print(json2cortex)

    return json_aux