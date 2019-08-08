import json

with open("json_sonion_to_thehive.json", "r") as read_file:
    data = json.load(read_file)

output = {
   "label": "[" + data["source"] + ":" + data["sourceRef"] + "] " + data["title"],
   "data": {
      "severity": data["severity"],
      "date": data["date"],
      "_routing": "6915e3521e23e9ad008a4ff101997dcf - GET id FROM THEHIVE",
      "customFields": {},
      "caseTemplate": "None" + " ???",
      "_type": "alert",
      "description": data["description"],
      "lastSyncDate": "1564596124743" + " ???",
      "source": data["source"],
      "title": data["title"],
      "type": data["type"],
      "follow": True,
      "tags": data["tags"],
      "createdAt": "1564596124743" + " ???",
      "_parent": None,
      "createdBy": "eco - GET createdBy FROM THEHIVE",
      "tlp": data["tlp"],
      "_id": "6915e3521e23e9ad008a4ff101997dcf - GET id FROM THEHIVE",
      "id": "6915e3521e23e9ad008a4ff101997dcf - GET id FROM THEHIVE",
      "sourceRef": data["sourceRef"],
      "_version": "1" + " - ???",
      "artifacts": data["artifacts"],
      "status": "New - GET status FROM THEHIVE"
   },
   "dataType": "thehive:alert - always the same??",
   "tlp": "2" + " - ???",
   "pap": "2" + " - ???",
   "message": "",
   "parameters": {
      "user": "eco - GET user FROM THEHIVE"
   }
}

with open("output.json", "w") as write_file:
    json.dump(output, write_file, indent=4)
