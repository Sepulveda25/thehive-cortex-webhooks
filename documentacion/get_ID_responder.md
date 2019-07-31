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
def web_application_attack(data):

    print("Busco ID del responder")

    cortexURL = 'http://172.16.81.110:9001'  # Your Cortex URL
    responder_name = 'MailsExcel'
    id_responder = 0

    search_url =  cortexURL + '/api/responder/_search?range=all'

    search_headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr"
               }

    search_data = {"query":{"dataTypeList":"thehive:alert"}}

    r = requests.post(search_url, data=json.dumps(search_data), headers=search_headers)
    json_response = r.json()



    #print(json_response)
    #Busco adentro del array el coincide con el responder con el opeardor "in"
    for i in json_response:
        if (responder_name in i['name']):
            id_responder = i['id']
            break


    print(id_responder)




