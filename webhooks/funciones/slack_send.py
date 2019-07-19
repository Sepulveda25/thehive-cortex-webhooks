#!/usr/bin/python3

from parametros import *

def slack_send(data): # New case observable created
   r = requests.post(hookURL, data, headers=headers)
   "Response: " + str(r.status_code) + "," + str(r.reason)
