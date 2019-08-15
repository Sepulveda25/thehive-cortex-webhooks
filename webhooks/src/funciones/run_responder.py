from parametros import *
import json

#Ejecuto un responder en base a su ID y un JSON de entrada (de la forma json_thehive_to_cortex)

def run_responder(json_thehive_to_cortex, id_responder):

    # url = 'http://172.16.81.110:9001/api/responder/29165d3c9329be9dd8a439fc1d4a1d66/run' #ejemplo
    url = cortexURL + '/api/responder/' + id_responder + '/run'
    # print(url)

    # header para la solicitud
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr"
    }


    #Ejecuto Json Cortex
    r = requests.post(url, data=json.dumps(json_thehive_to_cortex), headers=headers)
    # print(r.content)

    # Buscamos ID de la operacion run responder
    r_json = json.loads(r.content)
    id_responder_execution =  r_json['id']
    #print (id_responder)

    #Solicito confirmacion de ejecucion del responder

    url_waiting_report = cortexURL + '/api/job/' + id_responder_execution + '/waitreport?atMost=60000000000%20nanoseconds'
    r_waiting_report = requests.get(url_waiting_report,  headers=headers)
    # ".content" devuelve el contenido de la respuesta a la solicitud
    return r_waiting_report.content

