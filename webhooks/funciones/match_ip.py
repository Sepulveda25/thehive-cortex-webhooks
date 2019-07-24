#!/usr/bin/python3

from parametros import *

#recibe un json y matchea si alguna ip es interna

def match_ip(data): # New case observable created
   r = requests.post(hookURL, data, headers=headers)
   "Response: " + str(r.status_code) + "," + str(r.reason) 
