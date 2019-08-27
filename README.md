# Instalacion Webhooks para TheHive y respuesta automatica a alertas


## Tabla de contenidos

1. [Pre requisitos](#pre-requisitos)
2. [Instrucciones de instalacion](#instrucciones-de-instalacion)
3. [Instrucciones de testeo rapido](#instrucciones-de-testeo-rapido)
4. [Agregar respuesta automatica personalizada](#agregar-respuesta-automatica-personalizada)
4. [Referencias](#referencias)



## Pre requisitos

- Python 3.6
- Tener TheHive instalado, agregar al archivo application.conf (`/etc/thehive/application.conf`):

```
#The Hive Hooks local
webhooks {
  myLocalWebHook {
    url = "http://my_HTTP_endpoint/webhook"
  }
}
```

- Las reglas de ElastAlert deben incluir los `campos alert, category y classification` como `observables`, un ejemplo de regla es:
    

```

es_host: elasticsearch
es_port: 9200
# (Required)
# Rule name, must be unique
index: "*:logstash-ids-*"
name: Alerta de Aplicaciones Web Hive

type: frequency
num_events: 5
timeframe:
    minutes: 3
realalert:
    minutes: 0


filter:
- query_string:
    query: 'classification:"Web Application Attack"'

alert: hivealerter

hive_connection:
  hive_host: http://172.16.81.110
  hive_port: 9000
  hive_apikey: xLuixewzDP6zXcVgLvyaFUoeUZcZgKu3

hive_proxies:
  http: ''
  https: ''

hive_alert_config:
  title: '{rule[name]} -- {match[alert]}'
  type: 'external'
  source: 'SecurityOnion'
  description: '{match[message]}'
  severity: 3
  tags: ['elastalert, SecurityOnion, {match[category]}']
  tlp: 3
  status: 'New'
  follow: True

hive_observable_data_mapping:
  - source_ip: '{match[source_ip]}'
  - destination_ip: '{match[destination_ip]}'
  - source_port: '{match[source_port]}'
  - destination_port: '{match[destination_port]}'
  - interface: '{match[interface]}'
  - timestamp: '{match[@timestamp]}'
  - alert: '{match[alert]}'
  - category: '{match[category]}'	
  - classification: '{match[classification]}'
```

- Crear en TheHive los `observables: alert, category y classification`.


## Instrucciones de instalacion

(Para ver detalles del desarollo ver archivo `Instrucciones de desarollo` en carpeta Documentacion).


1.  Pegar carpeta webhooks en home y acceder a dicha carpeta.
2.  Eliminar carpeta `webhooksenv` en caso de existir.
3. Crear entorno virtual:
    <br />`$ python3.6 -m venv webhooksenv`
4.  Activar entorno virtual:
	<br />`$ source webhooksenv/bin/activate`
5.  Instalar librerias Flask, Gunicorn, Wheel, Request y Netaddr:
	<br />`$ pip install wheel`
	<br />`$ pip install gunicorn`
	<br />`$ pip install flask`
	<br />`$ pip install requests`
    <br />`$ pip install netaddr`
    <br />`$ pip install thehive4py`
6.  Salir del entorno virtual:
    <br />`$ deactivate`
7.  Permitir acceso puerto 5000:
	<br />`$ sudo ufw allow 5000`
8.  Dentro de la carpeta webhooks modificar el archivo `parametros.py` con los valores de `hiveUR`L y `hookURL` correspodientes.
9.  Copiar archivo `webhooks.service` en `/etc/systemd/system/`
10. Iniciar el servicio:
	<br />`$ sudo systemctl start webhooks.service`
11. Comprobar el estado del servicio:
	<br />`$ sudo systemctl enable webhooks.service`
12. Modificar TheHive para que envie acciones al ENDPOINT HTTP creado, agregando al archivo `/etc/thehive/application.conf`:

```
webhooks {
  myLocalWebHook {
    url = "http://my_HTTP_endpoint/webhook"
  }
}
```


## Instrucciones de testeo rapido

(Para ver detalles del desarollo ver archivo `Instrucciones de desarollo` en carpeta Documentacion).

Una vez realizados los pasos del apartado `Instrucciones de instalacion`:

1.  Dar de baja el servicio `webhooks.service` creado en la etapa `Instrucciones de instalacion`:
    <br />`$ sudo systemctl stop webhooks.service`
2. Dentro de la carpeta webhook activar entorno virtual:
    <br />`$ source webhooksenv/bin/activate`
3. Ejecutar programa principal con python:
    <br />`$  python theHiveWebhook.py`
4.  Al finaliza desactivar entorno virtual:
    <br />`$ deactivate`
5.  Reactivar servicio si se lo desea:
 	<br />`$ sudo systemctl start webhooks.service`


Se puede usar el ejemplo `crear_alerta_api` de la carpeta Documentacion para testear TheHive
(cambiar el campo sourceref cada vez que se ejecuta).



## Agregar respuesta automatica personalizada: 

1.  Dar de baja el servicio `webhooks.service` creado en la etapa `Instrucciones de instalacion`:
    <br />`$ sudo systemctl stop webhooks.service`
2.  Modificar el archivo `theHiveWebhook.py` (se muestra una parte del codigo): 

    ```
    if (imput_json['objectType']) == 'alert': # Creacion de alertas
        if (imput_json['operation']) == 'Creation':

            # dentro del array artifacts tenemos alert, category y classification!

            artifacts = imput_json['object']['artifacts']

            description_alert = None
            description_category = None
            description_classification = None

            # para cada objeto de la lista artifacts filtro por la
            # linea que tiene destination_ip como ip.
            for element in artifacts:
                if element["dataType"] == "alert":
                    description_alert = element["data"]
                if element["dataType"] == "category":
                    description_category = element["data"]
                if element["dataType"] == "classification":
                    description_classification = element["data "]

            if (description_alert.find("SQL Injection Attempt") > 0): #ejecuto la accion para la categoria
                SQL_injection_attempt(imput_json)
            #else if (description.find("Mi categoria 1") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(imput_json)
            #else if (description.find("Mi categoria 2") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(imput_json)
    ```
     
    Descomentar las lineas (o agregar una nueva comparacion en el if):
    
    <br># else if (description.find("mi_categoria_1 ") > 0): 
    <br># mi_respuesta_automatica_1(imput_json)
    <br>
    <br>- `mi_categoria_1`: es la categoria a la cual queremos responder automaticamente. Ejemplo: web application attack
    <br>- `mi_respuesta_automatica_1(imput_json)`: es la funcion de un programa en python `mi_respuesta_automatica_1.py` que ejecutara la respuesta deseada (almacenar el mismo en `src/categorias`)
    
3. El programa `mi_respuesta_automatica_1.py` se almacena en `scr/categorias`
4. Importar el programa `mi_respuesta_automatica_1` en `theHiveWebhook.py` agregando a la seccion de imports:
    <br>` import mi_respuesta_automatica_1`
5. El programa podra ejecutar apps de la carpeta `funciones` en caso de desearlo, por ejemplo:
     
    ```
    #!/usr/bin/python3
    
    # Toma una alerta con categoria "mi_respuesta_automatica_1" y corre automaticamente un responder
    # con la funcion run_responder
    
    import sys
    sys.path.insert(0, '../funciones')
    from run_responder import *
    
    def mi_respuesta_automatica_1(data):
    
    # Nombre del responder a ejectuar
    
        responder_name = 'nombreDelResponder'
 
        response = run_responder(data, responder_name)
    #    print (response)


    ```
6. Se puede usar 'testeo rapido' para verificar el funcionamiento del mismo (con el JSON adecuado)
7. Reactivar servicio si se lo desea:
 	<br />`$ sudo systemctl start webhooks.service`


## Referencias

* https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md#configuration
* https://github.com/TheHive-Project/TheHiveHooks
* https://github.com/cybergoatpsyops/TheHive-SideProjects
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
* https://github.com/TheHive-Project/TheHive4py/blob/master/thehive4py/api.py

