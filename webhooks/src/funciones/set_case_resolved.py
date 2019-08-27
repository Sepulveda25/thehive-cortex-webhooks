from parametros import *
import requests
import json
import sys
from pprint import pprint


try:
    from thehive4py.api import TheHiveApi
except ImportError:
    sys.exit(1)

def set_case_resolved(alert_id):

    api = TheHiveApi(hiveURL, apiKey, None, {'http': '', 'https': ''})

    case_promote_alert = api.promote_alert_to_case(alert_id).content


# Obtengo ID del caso
    case_json = json.loads(case_promote_alert)
    case_id = case_json["id"]
    case_idCase = case_json["caseId"]
#    print(case_id)
#    print(case_idCase)

# Ponemos el caso resuelto

    case = api.case(case_id)

    case.status = 'Resolved'
    case.resolutionStatus = 'TruePositive'
    case.impactStatus = 'NoImpact'
    case.summary = 'Resuelto automaticamente por The Hive Webhooks'

    hiveResponse = api.update_case(case, ['status', 'resolutionStatus', 'impactStatus', 'tags', 'summary'])


