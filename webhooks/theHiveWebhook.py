#!/usr/bin/python3
# https://github.com/cybergoatpsyops/TheHive-SideProjects

from parametros import *

import sys
sys.path.insert(0, './funciones')

from alerts import alert_new
from cases import case_new, case_delete, case_update
from tasks import task_new, task_update, task_delete, task_complete
from observers import observe_new, observe_update, observe_delete
from respuesta_automatica import *
from slack_send import slack_send

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

#nueva funcion para la alerta.


app = Flask(__name__)


@app.route('/', methods=['POST'])  # Flask app route
def process():  # If logic
    data = json.loads(request.data.decode("utf-8"))  # decode json data to utf-8 string
    keys = "objectType", "operation", "status"

    for k in keys:
        keypath, val = next(find_key(data, k))
        print("{!r}: {!r}".format(k, val))
    if (data['objectType']) == 'case':
        if (data['operation']) == 'Creation':  # Case created, updated, deleted
            post = case_new()
            slack_send(post)
            print (post)
        elif (data['operation']) == 'Update':            
            post = case_update()
            slack_send(post)
            print (post)
        elif (data['operation']) == 'Delete':
            post = case_delete()
            slack_send(post)
            print (post)
    if (data['objectType']) == 'case_task': # Task created deleted, completed, updated
        if (data['operation']) == 'Creation':        
            post = task_new()
            slack_send(post)
            print (post)
        elif (data['object']['status']) == 'Cancel':        
            post = task_delete()
            slack_send(post)
            print (post)
        elif (data['object']['status']) == 'Completed':         
            post = task_complete()
            slack_send(post)
            print (post)
        elif (data['operation']) == 'Update':
            if (data['object']['status']) == 'InProgress':
                post = task_update()
                slack_send(post)
                print (post)         
    if (data['objectType']) == 'case_artifact': # Observable created, updated, deleted
        if (data['operation']) == 'Creation':
            post = observe_new()
            slack_send(post)
            print (post)            
        elif(data['operation']) == 'Update':
            post = observe_update()
            slack_send(post)
            print (post)   
        elif (data['operation']) == 'Delete':
            post = observe_delete()
            slack_send(post)
            print (post)
    if (data['objectType']) == 'alert': # Creacion de alertas
        if (data['operation']) == 'Creation':
            #post = alert_new()
            #slack_send(post)
            #print (post)
            respuesta_automatica() #activa la respuesta
    return 'ok'


if __name__ == '__main__':
    app.run()

