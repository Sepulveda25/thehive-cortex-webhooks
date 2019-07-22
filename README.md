#  Pre-requisitos:

- Python 3.6

#  Instrucciones:

(Para ver detalles del desarollo ver archivo `Instrucciones de desarollo` en carpeta Documentacion).


1.  Pegar carpeta webhooks en home.
2.  Eliminar carpeta `webhooksenv` en caso de existir.
3. Crear entorno virtual:
    <br />`$ python3.6 -m venv webhooksenv`
4.  Activar entorno virtual:
	<br />`$ source webhooksenv/bin/activate`
5.  Instalar librerias Flask, Gunicorn, Wheel y Request:
	<br />`$ pip install wheel`
	<br />`$ pip install gunicorn`
	<br />`$ pip install flask`
	<br />`$ pip install requests`
6.  Salir del entorno virtual:
    <br />`$ deactivate`
7.  Permitir acceso puerto 5000:
	<br />`$ sudo ufw allow 5000`
8.  Dentro de la carpeta webhooks modificar el archivo `parametros.py` con los valores de `hiveUR`L y `hookURL` correspodientes.
9.  Copiar archivo `webhooks.service` en `/etc/systemd/system/`
10.   Iniciar el servicio:
	<br />`$ sudo systemctl start webhooks.service`
11.  Comprobar el estado del servicio:
	<br />`$ sudo systemctl enable webhooks.service`


#  Referencias:

* https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md#configuration
* https://github.com/TheHive-Project/TheHiveHooks
* https://github.com/cybergoatpsyops/TheHive-SideProjects
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04


