#!/usr/bin/python3

# Toma una alerta con categoria "web_application_attack" y corre automaticamente un responder
#

import sys
sys.path.insert(0, '../funciones')
from run_responder import *

def SQL_injection_attempt(data):


#    print (data)

# Nombre del responder a ejectuar

    responder_name = 'slackNotificacion'

    response = run_responder(data, responder_name)
#    print (response)


















