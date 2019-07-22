#  Pre-requisitos:

Python 3.6

#  Instrucciones:

(Para ver detalles del desarollo ver archivo Instrucciones completas en carpeta Documentacion).

1) Pegar carpeta webhooks en home.
2) Eliminar carpeta "webhooksenv" en caso de existir
3) Crear entorno virtual:
	$ python3.6 -m venv webhooksenv
4) Activar entorno virtual:
	$ source webhooksenv/bin/activate
5) Instalar Flask, Gunicorn, Wheel y requests:
	$ pip install wheel
	$ pip install gunicorn
	$ pip install flask
5) Permitir acceso puerto 5000:
	$ sudo ufw allow 5000 
6) Dentro de la carpeta webhooks modificar el archivo theHiveWebhook.py con los valores de hiveURL y hookURL correspodientes.
7) Copiar archivo webhooks.service en /etc/systemd/system/
8) Iniciar el servicio:
	$ sudo systemctl start webhooks.service
9) Comprobar el estado del servicio:
	$ sudo systemctl enable webhooks.service

#  Referencias:

https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md#configuration

https://github.com/TheHive-Project/TheHiveHooks

https://github.com/cybergoatpsyops/TheHive-SideProjects

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
