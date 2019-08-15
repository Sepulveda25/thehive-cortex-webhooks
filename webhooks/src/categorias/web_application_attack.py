#!/usr/bin/python3


from parametros import *

import sys
sys.path.insert(0, '../funciones')
from hive2cortex import *
from get_ID_responder import *
from run_responder import *

def web_application_attack(data):

#    print("Busco ID del responder")

#    print (data)

    responder_name = 'slackNotificacion'
    id_responder = get_ID_responder(responder_name)
#    print(id_responder)

# Transformo json de thehive a json de cortex
    hive2cortex_json = hive2cortex(data)
# print (hive2cortex_json

    json_output = run_responder(hive2cortex_json, id_responder)

    print (json_output)









