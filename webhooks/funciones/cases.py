#!/usr/bin/python3

from parametros import *

def case_new():  # New case created payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "New Hive Case",
            "pretext": "Case#" + (str(data['object']['caseId'])),
            "author_name": "Created by " + (str(data['object']['createdBy'])),
            "title": (str(data['details']['title'])),
            "title_link": hiveURL + "/index.html/case/" + data['objectId'] + "/details",
            "color": "danger",
            "text": "New Case Created!",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['details']['description'])),
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


def case_delete():  # Case deleted payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Hive Case Deleted",
            "pretext": "Case#" + (str(data['details']['caseId'])),
            "author_name": "Owner: " + (str(data['details']['owner'])),
            "title": (str(data['details']['title'])),
            "title_link": hiveURL + "/index.html#/cases",
            "color": "danger",
            "fields": [
                {
                    "title": "Description",
                    "value": "Case has been deleted",
                    "short": False
                }
            ]
        }
    ]
    }
    data=json.dumps(payload)
    return data 
 #   r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
 #   "Response: " + str(r.status_code) + "," + str(r.reason)


def case_update():  # Case updated payload
    data = json.loads(request.data.decode('utf-8'))
    payload = {"attachments": [
        {
            "fallback": "Hive Case Updated",
            "pretext": "New Case Update - " + (str(data['object']['title'])),
            "author_name": "Updated by " + (str(data['object']['updatedBy'])),
            "title": (str(data['object']['title'])),
            "title_link": hiveURL + "/index.html#/case/" + data['objectId'] + "/details",
            "color": "danger",
            "fields": [
                {
                    "title": "Description",
                    "value": (str(data['details']['description'])),
                    "short": False,
                }
            ]
        }
    ]
    }
    data=json.dumps(payload)
    return data 
 #   r = requests.post(hookURL, data=json.dumps(payload), headers=headers)
 #   "Response: " + str(r.status_code) + "," + str(r.reason)
