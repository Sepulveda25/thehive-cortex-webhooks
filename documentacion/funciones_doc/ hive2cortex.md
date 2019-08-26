# Ejecutar responder

## Tabla de contenidos

1. [Introduccion](#introduccion)
2. [Codigo en Python](#codigo-en-python)


## Introduccion

Funcion encargada de convertir el JSON de entrada a TheHhive (ver en carpeta 



## Codigo en Python

`run_responder.py`

```
import json

#Ejecuto un responder en base a su ID y un JSON de entrada (de la forma json_thehive_to_cortex)

def run_responder(json_thehive_to_cortex, id_responder):

    url = cortexURL + '/api/responder/' + id_responder + '/run'

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr"
    }


    #Ejecuto Json Cortex
    r = requests.post(url, data=json.dumps(json_thehive_to_cortex), headers=headers)

    # Buscamos ID de la operacion run responder
    r_json = json.loads(r.content)
    id_responder_execution =  r_json['id']

    #Solicito confirmacion de ejecucion del responder

    url_waiting_report = cortexURL + '/api/job/' + id_responder_execution + '/waitreport?atMost=60000000000%20nanoseconds'
    r_waiting_report = requests.get(url_waiting_report,  headers=headers)
    # ".content" devuelve el contenido de la respuesta a la solicitud
    return r_waiting_report.content 
```



