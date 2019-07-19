#!/usr/bin/python3

from flask import Flask, request
import json
import requests
import os

hookURL = 'https://hooks.slack.com/services/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'  # Your Slack URL API
hiveURL = 'http://172.16.81.110'  # Your Hive URL
headers = {'content-type': 'application/json'}

