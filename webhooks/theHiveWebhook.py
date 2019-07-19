#!/usr/bin/python3
# https://github.com/cybergoatpsyops/TheHive-SideProjects

from parametros import *

import sys
sys.path.insert(0, './funciones')

from alerts import alert_new
from cases import case_new, case_delete, case_update
from observers import observe_new, observe_update, observe_delete

hookURL = 'https://hooks.slack.com/services/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'  # Your Slack URL API
hiveURL = 'http://172.16.81.110'  # Your Hive URL
headers = {'content-type': 'application/json'}


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
            case_new()
        elif (data['operation']) == 'Update':
            case_update()
        elif (data['operation']) == 'Delete':
            case_delete()
    if (data['objectType']) == 'case_task': # Task created deleted, completed, updated
        if (data['operation']) == 'Creation':
            task_new()
        elif (data['object']['status']) == 'Cancel':
            task_delete()
        elif (data['object']['status']) == 'Completed':
            task_complete()
        elif (data['operation']) == 'Update':
            if (data['object']['status']) == 'InProgress':
                task_update()
    if (data['objectType']) == 'case_artifact': # Observable created, updated, deleted
        if (data['operation']) == 'Creation':
            observe_new()
        elif(data['operation']) == 'Update':
            observe_update()
        elif (data['operation']) == 'Delete':
            observe_delete()
    if (data['objectType']) == 'alert': # Creacion de alertas
        if (data['operation']) == 'Creation':
            alert_new()
    return 'ok'


if __name__ == '__main__':
    app.run()
