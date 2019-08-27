from parametros import *
import json

from hive2cortex import *
from get_ID_responder import *
from set_case_resolved import *

#Ejecuto un responder en base a su ID y un JSON de entrada (de la forma json_thehive_to_cortex)

def run_responder(data, responder_name):


    # Obtengo ID responder
    id_responder = get_ID_responder(responder_name)
    #  print(id_responder)

    # Transformo json de thehive a json de cortex
    json_thehive_to_cortex = hive2cortex(data)
    # print (json_thehive_to_cortex)

    # Creo URL
    url = cortexURL + '/api/responder/' + id_responder + '/run'
    # print(url)

    #Ejecuto Json Cortex mediante POST
    r = requests.post(url, data=json.dumps(json_thehive_to_cortex), headers=headers)
    # print(r)
    # print(r.content)

    # Buscamos ID de la operacion run responder
    r_json = json.loads(r.content)
    id_responder_execution =  r_json['id']
    #print (id_responder)

    #Solicito confirmacion de ejecucion del responder
    url_waiting_report = cortexURL + '/api/job/' + id_responder_execution + '/waitreport?atMost=60000000000%20nanoseconds'
    r_waiting_report = requests.get(url_waiting_report,  headers=headers)
    #print (r_waiting_report.content)

    # Verficamos si la ejecucion del responder es correcta (report - > success = true)
    r_waiting_report_json = json.loads(r_waiting_report.content)
    success = str( r_waiting_report_json['report']['success']) # convierto json value en string
    #    print (success)


    # Creamos una entrada en TheHive de caso resuelto
    # Primero obtenemos el ID (object -> id)
    id_alert = data['object']['id']
    #print (id_alert)
    if(success is "True"):
        set_case_resolved(id_alert)

    return "ok"

