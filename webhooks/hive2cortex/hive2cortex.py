import argparse
import configparser
import json
import os
import sys
import requests

try:
    from thehive4py.api import TheHiveApi
    from thehive4py.models import Alert, AlertArtifact
except ImportError:
    sys.exit(1)

# Default configuration
args = ''
config = {
    'thehiveURL': '',
    'thehiveApiKey': '',
}


def main():
    global args
    global config

    parser = argparse.ArgumentParser(
        description='TODO.')
    parser.add_argument('-c', '--config',
                        dest='configFile',
                        help='configuration file (default: ./hive2cortex.conf)',
                        metavar='CONFIG')
    parser.add_argument('-i', '--input',
                        dest='inputFile',
                        help='input file (default: ./input.json)',
                        metavar='input')
    parser.add_argument('-o', '--output',
                        dest='outputFile',
                        help='output file (default: ./output.json)',
                        metavar='OUTPUT')
    args = parser.parse_args()

    # Default values
    if not args.configFile:
        args.configFile = './hive2cortex.conf'
    if not args.inputFile:
        args.inputFile = './input.json'
    if not args.outputFile:
        args.outputFile = './output.json'

    if not os.path.isfile(args.configFile):
        print('Configuration file %s is not readable.' % args.configFile)
        sys.exit(1)
    if not os.path.isfile(args.inputFile):
        print('Input file %s is not readable.' % args.inputFile)
        sys.exit(1)

    try:
        conf_file = configparser.ConfigParser()
        conf_file.read(args.configFile)
    except OSError as e:
        print('Cannot read config file %s: %s' % (args.configFile, e.errno))
        sys.exit(1)

    # TheHive Config
    config['thehiveURL'] = conf_file.get('thehive', 'url')
    config['thehiveApiKey'] = conf_file.get('thehive', 'apikey')
    api = TheHiveApi(config['thehiveURL'], config['thehiveApiKey'], None, {'http': '', 'https': ''})

    response = json.load(api.get_alert(id))
    if response.status_code == requests.codes.ok:
        # print(json.dumps(response.json(), indent=4, sort_keys=True))
        print('')
    else:
        print("Error retreiving the alert!")
    print('ko: {}/{}'.format(response.status_code, response.text))

    # Json conversion
    with open(args.inputFile, "r") as read_file:
        input_data = json.load(read_file)
    output = {
        "label": "[" + input_data["source"] + ":" + input_data["sourceRef"] + "] " + input_data["title"],
        "data": {
            "severity": input_data["severity"],
            "date": input_data["date"],
            "_routing": "6915e3521e23e9ad008a4ff101997dcf - GET id FROM THEHIVE",
            "customFields": {},
            "caseTemplate": "None" + " ???",
            "_type": "alert",
            "description": input_data["description"],
            "lastSyncDate": "1564596124743" + " ???",
            "source": input_data["source"],
            "title": input_data["title"],
            "type": input_data["type"],
            "follow": True,
            "tags": input_data["tags"],
            "createdAt": "1564596124743" + " ???",
            "_parent": None,
            "createdBy": "eco - GET createdBy FROM THEHIVE",
            "tlp": input_data["tlp"],
            "_id": "6915e3521e23e9ad008a4ff101997dcf - GET id FROM THEHIVE",
            "id": "6915e3521e23e9ad008a4ff101997dcf - GET id FROM THEHIVE",
            "sourceRef": input_data["sourceRef"],
            "_version": "1" + " - ???",
            "artifacts": input_data["artifacts"],
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
    with open(args.outputFile, "w") as write_file:
        json.dump(output, write_file, indent=4)
        # print(json.dumps(output, indent=4, sort_keys=True))

    return


main()
