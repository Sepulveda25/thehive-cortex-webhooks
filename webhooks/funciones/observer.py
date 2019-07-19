#!/usr/bin/python3

from parametros import *

def observe_new(): # New case observable created
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Observable Created",
            "pretext": "Observable Created",
            "author_name": "Created by " + (str(data['object']['createdBy'])),
            "title": "New " + (str(data['object']['dataType'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/observables",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['object']['message'])),
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def observe_update():  # Case observable updated
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Observable Updated",
            "pretext": "Observable Updated",
            "author_name": "Updated by " + (str(data['object']['updatedBy'])),
            "title": "New " + (str(data['object']['dataType'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/observables",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['object']['message'])),
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)


def observe_delete():  # Case obserable deleted
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Observable Deleted",
            "pretext": "Observable Deleted",
            "author_name": "Deleted by " + (str(data['object']['updatedBy'])),
            "title": "New " + (str(data['object']['dataType'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/observables",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Observable has been permanently deleted",
                    "short": False
                }
            ]
        }
    ]
    }
    r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
    "Response: " + str(r.status_code) + "," + str(r.reason)
