#!/usr/bin/python3
# https://github.com/cybergoatpsyops/TheHive-SideProjects

from parametros import *

import sys
sys.path.insert(0, './src/categorias')
sys.path.insert(0, './src/funciones')
from SQL_injection_attempt import *
from match_ip_internal import *

def find_key(obj, key):  # recursive generator
    if isinstance(obj, dict):
        yield from iter_dict(obj, key, [])
    elif isinstance(obj, list):
        yield from iter_list(obj, key, [])


def iter_dict(d, key, indices):
    for k, v in d.items():
        if k == key:
            yield indices + [k], v
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])


def iter_list(seq, key, indices):
    for k, v in enumerate(seq):
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])


app = Flask(__name__)


@app.route('/', methods=['POST'])  # Flask app route
def process():  # If logic
    imput_json = json.loads(request.data.decode("utf-8"))  # decode json data to utf-8 string
    keys = "objectType", "operation", "status"

    for k in keys:
        keypath, val = next(find_key(imput_json, k))
        print("{!r}: {!r}".format(k, val))

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
                    #print ("description_alert: " + description_alert)
                if element["dataType"] == "category":
                    description_category = element["data"]
                    #print ("description_category: " + description_category)
                if element["dataType"] == "classification":
                    description_classification = element["data"]
                    #print ("description_classification: " + description_classification)

            #ESTO SE USA?
            is_internal =  match_ip_internal (imput_json)

            if (description_alert.find("SQL Injection Attempt") > 0): #ejecuto la accion para la categoria
                SQL_injection_attempt(imput_json)
            #else if (description.find("Mi categoria 1") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(imput_json)
            #else if (description.find("Mi categoria 2") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(imput_json)

    return 'ok'


if __name__ == '__main__':
    app.run()

