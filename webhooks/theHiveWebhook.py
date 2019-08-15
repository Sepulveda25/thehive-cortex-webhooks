#!/usr/bin/python3
# https://github.com/cybergoatpsyops/TheHive-SideProjects

from parametros import *

import sys
sys.path.insert(0, './src/categorias')
sys.path.insert(0, './src/funciones')
from web_application_attack import *
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

            # en el campo description tenemos category!
            description = imput_json['object']['description']
            #  print ("description: " + description)

            #FALTA COMPROBAR SI ES INTERNAL IP

            if (description.find("Web Application Attack") > 0): #ejecuto la accion para la categoria
                web_application_attack(imput_json)
            #else if (description.find("Mi categoria 1") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(data)
            #else if (description.find("Mi categoria 2") > 0): #ejecuto la accion para la categoria
            #    mi_respuesta_automatica_1(data)

    return 'ok'


if __name__ == '__main__':
    app.run()

