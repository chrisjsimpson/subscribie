import requests
import os
import json
from flask import current_app as app

def get_csrf_token():
    #Get CSRF token
    token = str(requests.get(app.config['PENGUIN_URL'] + '/session/token').text)
    return token

def get_headers():
    #Set all required headers
    headers = {'Content-Type':'application/hal+json',
	'X-CSRF-Token':get_csrf_token()
    }
    return headers


def format_fields(fields):
    fields_formatted = {}
    for index, value in enumerate(fields):
        fields_formatted[value] = [{"value": fields[value]}]
    #Convert to json
    fields_formatted = json.dumps(fields_formatted)
    #Remove outer brackets and return
    return fields_formatted[1:-1]

def post(fields='', entity=''):
    print "Posting to penguin!"

    endpoint = app.config['PENGUIN_URL'] + "/node?_format=hal_json"
    entity_href = ''.join(['"', app.config['PENGUIN_URL'], '/rest/type/node/', entity,'"'])
    # Replace https with http for entity href only (endpoint remains https)
    entity_href = entity_href.replace('https','http')

    #Set all required headers
    headers = get_headers()

    #Include all fields required by the content type
    payload  = '''
    {
    "_links": {
    "type": {
    "href": '''
    payload = payload + entity_href
    payload = payload + '''
    }
    },'''
    payload = payload + format_fields(fields) + '''
    }'''

    #Post the new node (a Contact) to the endpoint.
    user = app.config['REST_USER']
    password = app.config['REST_PASSWORD']
    r = requests.post(endpoint, data=payload, headers=headers, auth=(user,password))

    #Check was a success 
    if r.status_code == 201:
	print "Success"
        print r.text
        return r
    else:
	print "Fail"
	print r.status_code
        print r.text
        return r

def patch(nid, entity, fields):
    print "Patching to Penguin!"

    endpoint = app.config['PENGUIN_URL'] + "/node/" + str(nid) + "?_format=hal_json"
    entity_href = ''.join(['"', app.config['PENGUIN_URL'], '/rest/type/node/', entity,'"'])
    # Replace https with http for entity href only (endpoint remains https)
    entity_href = entity_href.replace('https','http')

    #Set all required headers
    headers = get_headers()

    #Include all fields required by the content type
    payload  = '''
    {
    "_links": {
    "type": {
    "href": '''
    payload = payload + entity_href
    payload = payload + '''
    }
    },'''
    payload = payload + format_fields(fields) + '''
    }'''

    #Post the new node (a Contact) to the endpoint.
    user = app.config['REST_USER']
    password = app.config['REST_PASSWORD']
    r = requests.patch(endpoint, data=payload, headers=headers, auth=(user,password))

    #Check was a success 
    if r.status_code == 200:
	print "Patch Successful"
	print r.status_code
        print r.text
        return r
    else:
	print "Patch Fail"
	print r.status_code
        print r.text
        return r
