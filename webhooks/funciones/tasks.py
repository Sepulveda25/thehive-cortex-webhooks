#!/usr/bin/python3

from parametros import *

def task_new():  # New case task created payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "New Case Task",
            "pretext": "New Case Task",
            "author_name": "Created by " + (str(data['object']['createdBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "New task has been created",
                    "short": False
                }
            ]
        }
    ]
    }
    data=json.dumps(payload)
    return data 
   # r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
   # print("Response: " + str(r.status_code) + "," + str(r.reason))


def task_update():  # Case task updated payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Task Update",
            "pretext": "Task Update",
            "author_name": "Updated by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been updated",
                    "short": False
                }
            ]
        }
    ]
    }
    data=json.dumps(payload)
    return data 
   # r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
   # print("Response: " + str(r.status_code) + "," + str(r.reason))


def task_delete():  # Case task deleted payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Task Canceled",
            "pretext": "Task Canceled",
            "author_name": "Canceled by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been canceled",
                    "short": False
                }
            ]
        }
    ]
    }
    data=json.dumps(payload)
    return data 
   # r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
   # print("Response: " + str(r.status_code) + "," + str(r.reason))


def task_complete():  # Case task completed payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Task Completed",
            "pretext": "Task Completed",
            "author_name": "Completed by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/tasks",
            "color": "warning",
            "fields": [
                {
                    "title": "Description",
                    "value": "Task has been completed",
                    "short": False
                }
            ]
        }
    ]
    }
    data=json.dumps(payload)
    return data 
   # r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
   # print("Response: " + str(r.status_code) + "," + str(r.reason))
