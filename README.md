# Instalacion Webhooks para TheHive y respuesta automatica a alertas

#Tabla de contenidos

<!--ts-->
   * [Pre-requisitos](#Pre-requisitos)
   * [Instrucciones de instalacion](#Instrucciones de instalacion)
   * [Instrucciones de testeo rapido](#Instrucciones de testeo rapido)
   * [Referencias](#Referencias)
<!--te-->

## Pre-requisitos

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


Instrucciones de testeo rapido
=====

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



Referencias
=====

* https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md#configuration
* https://github.com/TheHive-Project/TheHiveHooks
* https://github.com/cybergoatpsyops/TheHive-SideProjects
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04


