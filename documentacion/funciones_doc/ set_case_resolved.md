# Obtener ID de un responder a traves de su nombre



## Tabla de contenidos

1. [Uso de la api thehive4py](#uso-de-la-api-thehive4py)
2. [Codigo en Python](#codigo-en-python)
3. [Referencias](#referencias)


## uso-de-la-api-thehive4py 

Se utiliza las apis provistas por thehive4py para promover una alerta a caso en 
TheHIVE y marcar dicho caso como resuelto de forma automatica.

La funcion promote_alert_to_case(self, alert_id) de thehive4py se usa para promover
la alerta a caso.

La funcion case(self, case_id) de thehive4py se usa para obtener el caso completo,
los campos del caso se acceden y modifican como:

<br />    case.status = 'Resolved'
<br />    case.resolutionStatus = 'TruePositive'
<br />    case.impactStatus = 'NoImpact'
<br />    case.summary = 'Resuelto automaticamente por The Hive Webhooks'

En el ejemplo anterior se modifican los campos status, resolutionStatus, impactStatus
y summary que son los campos tipicos que se modifican cuando se marca una alerta como resuelta.



## Codigo en Python 

`set_case_resolved.py`

```
from parametros import *
import requests
import json
import sys


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

# Ponemos el caso resuelto

    case = api.case(case_id)

    case.status = 'Resolved'
    case.resolutionStatus = 'TruePositive'
    case.impactStatus = 'NoImpact'
    case.summary = 'Resuelto automaticamente por The Hive Webhooks'

    hiveResponse = api.update_case(case, ['status', 'resolutionStatus', 'impactStatus', 'tags', 'summary'])
  
```


## Referencias



