# Ejecutar responder automaticamente

## Tabla de contenidos

1. [Analisis de mensajes intercambiados](#analisis-de-mensajes-intercambiados)
2. [Especificacion del programa](#especificacion-del-programa)
3. [Codigo en Python](#codigo-en-python)


## Analisis de mensajes intercambiados

Se detalla como TheHive ejecuta un Responder de Cortex en base al ID de mismo 
obtenido anteriormente (Este paso se detalla en el documento `get_ID_responder.md`).

Para ello se analiza los paquetes en Wireshark.

Para comenzar sniffeamos el trafico usando Wireshark en el servidor que
contiene TheHive, filtrando el puerto 9001 correspondiente a Cortex.

En la interfaz de TheHive activamos algun Responder (en este caso la alerta cuenta
con todos los observables que requiere el Responder).


![](imagenes/ejecucion_responder_1.png)


Luego se analiza el intercambio de mensajes entre TheHive y Cortex en Wireshark.


![](imagenes/ejecucion_responder_2.png)


TheHive envia una solicitud POST: 
`POST /api/responder/460d2164401c0079784ef0778eceb8ca/run`
(460d2164401c0079784ef0778eceb8ca es el ID del responder obtenido en los mensajes
anteriores, cuyo funcionamiento se detalla en el documento `get_ID_responder.md`)


![](imagenes/ejecucion_responder_3.png)


Dentro de este mensaje envia un JSON que tiene la forma del documento: 
`json_thehive_to_cortex.json`.


Cortex respode la solicitud enviando mensaje HTTP/1.1 200 OK. En el cual se incluye
un JSON de la forma del documento: `json_cortex_to_hive.json`, dentro hay un 
campo `id` (tambien los campos `_id` y `_routing` contienen la misma informacion), 
que inidica el ID de la ejecucion del responder. 

![](imagenes/ejecucion_responder_4.png)


Luego TheHive envia una solicitud GET, que contiene el ID de la ejecucion del 
responder (ejemplo: `AWyRuHfRrefEjDnmkcit`) el cual extrae en el JSON anterior, 
esto le permite obtener informacion sobre la ejecucion del responder (exitosa o no):

`GET /api/job/AWyRuHfRrefEjDnmkcit/waitreport?atMost=60000000000%20nanoseconds HTTP/1.1`


![](imagenes/ejecucion_responder_5.png)



Cortex responde a esta solucitud GET con un JSON que tiene la forma del documento:
`json_cortex_to_thehive_waitreport.json`, donde el campo report dentro del JSON 
indica si la ejecucion fue exitosa o no.

## Especificacion del programa

El programa realiza las siguientes actividades:

1.  Recibe como parametro `data` el JSON que proviene desde SONION y `responder_name` el nombre del responder a ejecutar.
2.  Llama a la funcion `get_ID_responder(responder_name)` y obtiene el ID del responder.
3.  Llama a la funcion hive2cortex(data) donde `data` es un JSON del tipo `json_sonion_to_thehive.json` y devuelve un JSON del tipo `json_thehive_to_cortex.json`
4.  Genera 
5.  4
6.  4
7.  2
8.  
9.  





## Codigo en Python

`run_responder.py`

```
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


```




