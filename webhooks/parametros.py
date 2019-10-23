#!/usr/bin/python3

from flask import Flask, request
import json
import requests
import os

hookURL = 'https://hooks.slack.com/services/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'  # Your Slack URL API
hiveURL = 'http://172.16.81.110:9000'  # Your Hive URL
cortexURL = 'http://172.16.81.110:9001'  # Your Cortex URL
# apiKey = 'xLuixewzDP6zXcVgLvyaFUoeUZcZgKu3'  # COlocar APIKEY usuario de thehive
headers = {'content-type': 'application/json'}
activosPSI = 'http://activos-api.psi.unc.edu.ar/assets?elasticSearch='
# header para la solicitud
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer baDVP07GJj7uOcWEp7sSpU+oJ42/GJKr" # COlocar APIKEY usuario de thehive
}