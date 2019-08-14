# Ejecutar responder

## Tabla de contenidos

1. [Analisis de mensajes intercambiados](#analisis-de-mensajes-intercambiados)
2. [Codigo en Python](#codigo-en-python)


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
un JSON de la forma del documento: `json_thehive_to_cortex.json`, dentro hay un 
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



## Codigo en Python

```
import json

def run_responder(imput_json, id_responder):

    url = cortexURL + '/api/responder/' + id_responder + '/run'

    # headers para la solicitud 
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr"
    }


    #Ejecuto Cortex con JSON imput

    r = requests.post(url, data=json.dumps(imput_json), headers=headers)

    #print(r.content)

    return r
```





