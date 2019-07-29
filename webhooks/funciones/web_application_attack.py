#!/usr/bin/python3

from parametros import *

def web_application_attack(data):

    print("Llamo al respoder correspondiente")

    #url = 'http://172.16.81.110:9001/api/responder/_search?range=all'
    url = 'http://172.16.81.110:9001/api/responder/29165d3c9329be9dd8a439fc1d4a1d66/run'

    headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr"
               }

    print(data)

    #datos = {"label":"[SecurityOnion:57ba6f] New IDS Alert! -- SURICATA SMTP invalid pipelined sequence ","data":{"severity":"3","date":"1564081498000","_routing":"f484b8ae64474689352604ccb9985f54","customFields":{},"caseTemplate":"null","_type":"alert","description":"[1:2220004:1] SURICATA SMTP invalid pipelined sequence [Classification: Generic Protocol Command Decode] [Priority: 3]: <sonion-virtual-machine-ens192> {TCP} 200.16.22.73:60916 -> 200.16.22.1:25","lastSyncDate":"1564081494991","source":"SecurityOnion","title":"New IDS Alert! -- SURICATA SMTP invalid pipelined sequence ","type":"external","follow":"true","tags":["elastalert, SecurityOnion, {match[category]}"],"createdAt":"1564081494990","_parent":"null","createdBy":"eco","tlp":"3","_id":"f484b8ae64474689352604ccb9985f54","id":"f484b8ae64474689352604ccb9985f54","sourceRef":"57ba6f","_version":"1","artifacts":[{"data":"200.16.22.73","dataType":"source_ip","message":"null","tags":[],"tlp":"2"},{"data":"200.16.22.1","dataType":"destination_ip","message":"null","tags":[],"tlp":"2"},{"data":"60916","dataType":"source_port","message":"null","tags":[],"tlp":"2"},{"data":"25","dataType":"destination_port","message":"null","tags":[],"tlp":"2"},{"data":"sonion-virtual-machine-ens192","dataType":"interface","message":"null","tags":[],"tlp":"2"},{"data":"2019-07-25T18:59:57.732Z","dataType":"timestamp","message":"null","tags":[],"tlp":"2"},{"data":"snort","dataType":"event_type","message":"null","tags":[],"tlp":"2"}],"status":"New"},"dataType":"thehive:alert","tlp":"2","pap":"2","message":"","parameters":{"user":"thehive"}}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r)



