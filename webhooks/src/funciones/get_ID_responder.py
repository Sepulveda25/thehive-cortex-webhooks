from parametros import *
import json

#transformo el JSON de entrada a TheHive a un JSON de entrada a Cortex

def get_ID_responder(responder_name):

    # cortexURL definido en paramtros.py
    search_url = cortexURL + '/api/responder/_search?range=all'
    id_responder = 0

    search_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr"
    }

    #parametros de consulta
    search_data = {"query": {"dataTypeList": "thehive:alert"}}

    r = requests.post(search_url, data=json.dumps(search_data), headers=search_headers)
    json_response = r.json()

    # print(json_response)
    # Busco adentro del array el que coincide con el nombre del responder
    for i in json_response:
        if (responder_name in i['name']):
            id_responder = i['id']
            break

    # ya tengo el ID del repsonder
    #print(id_responder)

    return id_responder