# Obtener ID de un responder a traves de su nombre

## Tabla de contenidos

1. [Analisis de mensajes intercambiados](#analisis-de-mensajes-intercambiados)
2. [Codigo en Python](#codigo-en-python)


## Analisis de mensajes intercambiados

Se detalla como TheHive obtiene el ID de un Responder de Cortex en base al 
nombre del Responder.

Para ello se analiza los paquetes en Wireshark.

Para comenzar sniffeamos el trafico usando Wireshark en el servidor que
contiene TheHive, filtrando el puerto 9001 correspondiente a Cortex.

En la interfaz de TheHive activamos algun Responder (en este caso la alerta cuenta
con todos los observables que requiere el Responder).


![](imagenes/obtener_ID_responder_1.png)


Luego se analiza el intercambio de mensajes entre TheHive y Cortex en Wireshark.


![](imagenes/obtener_ID_responder_2.png)


The Hive envia una solicitud POST: /api/responder/_search?range=all 


![](imagenes/obtener_ID_responder_3.png)


Cortex respode la solicitud enviando un JSON. Este JSON contiene un object para
cada Responder, de esta podemos analizar los campos Name hasta que coincida con
el nombre del Responder para luego obtener el valor del campo ID.


![](imagenes/obtener_ID_responder_4.png)


## Codigo en Python

```

import json


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




