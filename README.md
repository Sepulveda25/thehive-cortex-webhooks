Instrucciones:

(Para ver detalles del desarollo ver archivo Instrucciones completas en carpeta Documentacion).

1) Pegar carpeta webhooks en home.
2) Dentro de la carpeta webhooks modificar el archivo theHiveWebhook.py con los valores de hiveURL y hookURL correspodientes.
3) Copiar archivo webhooks.service en /etc/systemd/system/
4) Iniciar el servicio:
	$ sudo systemctl start webhooks.service
5) Comprobar el estado del servicio:
	$ sudo systemctl enable webhooks.service

Referencias:

https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhooks.md#configuration

https://github.com/TheHive-Project/TheHiveHooks

https://github.com/cybergoatpsyops/TheHive-SideProjects

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
