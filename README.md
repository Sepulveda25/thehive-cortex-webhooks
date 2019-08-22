# Instalacion Webhooks para TheHive y respuesta automatica a alertas


## Tabla de contenidos

1. [Pre requisitos](#pre-requisitos)
2. [Instrucciones de instalacion](#instrucciones-de-instalacion)
3. [Instrucciones de testeo rapido](#instrucciones-de-testeo-rapido)
4. 
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
5.  Reactivar servicio si se lo desea de acuerdo al `paso 10` del apartado `Instrucciones de instalacion`.


## Agregar respuesta automatica personalizada: 

1.  Dar de baja el servicio `webhooks.service` creado en la etapa `Instrucciones de instalacion`:
    <br />`$ sudo systemctl stop webhooks.service'
2.  Modificar o agregar al archivo `theHiveWebhook.py`: 

    
    ```
    if (imput_json['objectType']) == 'alert': # Creacion de alertas
        if (imput_json['operation']) == 'Creation':

            # en el campo description tenemos category!
            description = imput_json['object']['description']
            #  print ("description: " + description)

            #FALTA COMPROBAR SI ES INTERNAL IP

            if (description.find("Web Application Attack") > 0): #ejecuto la accion para la categoria
                web_application_attack(imput_json)
            #else if (description.find("Mi categoria 1") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(imput_json)
            #else if (description.find("Mi categoria 2") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(imput_json)
    ```
     
     en las lineas (descomentadas):
    <br> else if (description.find("Mi_categoria_1 ") > 0): #ejecuto la accion para la categoria
    <br> mi_respuesta_automatica_1(imput_json)
    <br>
    <br>-  Mi_categoria_1 es la categoria a la cual queremos responder automaticamente. Ejemplo: web application attack)
    <br>-  mi_respuesta_automatica_1 es el python que se ejecutara (almacenar el mismo en src/categorias)
    

3. h
4. h
5. f
6. d
7. s
8. s
9. s
10. ss
11. a
12. a


```
webhooks {
  myLocalWebHook {
    url = "http://my_HTTP_endpoint/webhook"
  }
}
```



Se puede usar el ejemplo `crear_alerta_api` de la carpeta Documentacion para testear TheHive
(cambiar el campo sourceref cada vez que se ejecuta).


## Referencias

* https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md#configuration
* https://github.com/TheHive-Project/TheHiveHooks
* https://github.com/cybergoatpsyops/TheHive-SideProjects
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
* https://github.com/TheHive-Project/TheHive4py/blob/master/thehive4py/api.py

