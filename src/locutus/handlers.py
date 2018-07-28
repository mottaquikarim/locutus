import logging
import time
import json
import uuid

from twilio.twiml.messaging_response import MessagingResponse
from urllib.parse import parse_qs

from locutus.conf import SUPPORTED_APPLIANCES
from locutus.appliances import get_endpoint_from_v3_appliance
from locutus.ecovacs import start, stop 

# Setup logger

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_resp(message):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/xml',
        },
        'body': str(message),
    }

def webhook_handler(event, context):
    logger.info('WEBHOOK request is {}'.format(json.dumps(event)))
    resp = MessagingResponse()

    body = parse_qs(event['body'])
    message = body.get('Body', [])
    if len(message) == 0:
        resp.message("Cannot process request")
        return get_resp(resp)

    message = message[0]

    if "vacuum" in message and "on" in message:
        start()
        resp.message("vacuum turned on")
    elif "vacuum" in message and "off" in message:
        stop()
        resp.message("vacuum turned off")
    else:
        resp.message("I don't know how to do that")

    return get_resp(resp)


def ecovacs_handler(request, context):
    logger.info('request is {}'.format(json.dumps(request)))
    if request['directive']['header']['name'] == 'Discover':
        response = handle_discovery_v3(request)
    else:
        response = handle_non_discovery_v3(request)
    return response


# v3 handlers

def handle_discovery_v3(request):
    endpoints = []
    for appliance in SUPPORTED_APPLIANCES:
        endpoints.append(get_endpoint_from_v3_appliance(appliance))

    response = {'event': {'header': {
        'namespace': 'Alexa.Discovery',
        'name': 'Discover.Response',
        'payloadVersion': '3',
        'messageId': str(uuid.uuid4()),
    }, 'payload': {'endpoints': endpoints}}}

    return response


def handle_non_discovery_v3(request):
    request_namespace = request['directive']['header']['namespace']
    request_name = request['directive']['header']['name']
    request_endpoint_name = request['directive']['endpoint']['endpointId']

    if request_namespace == 'Alexa.PowerController':
        if request_name == 'TurnOn':
            value = 'ON'
            if request_endpoint_name == 'ecovac':
                start()
        else:
            value = 'OFF'
            if request_endpoint_name == 'ecovac':
                stop()

        response = {'context': {'properties': [{
            'namespace': 'Alexa.PowerController',
            'name': 'powerState',
            'value': value,
            'timeOfSample': time.strftime('%Y-%m-%dT%H:%M:%S.00Z',
                                          time.gmtime()),
            'uncertaintyInMilliseconds': 500,
        }]}, 'event': {'header': {
            'namespace': 'Alexa',
            'name': 'Response',
            'payloadVersion': '3',
            'messageId': str(uuid.uuid4()),
            'correlationToken': request['directive']['header'
                                                     ]['correlationToken'],
        }, 'endpoint': {'scope': {'type': 'BearerToken',
                                  'token': 'access-token-from-Amazon'},
                        'endpointId': request['directive'
                                              ]['endpoint']['endpointId']},
            'payload': {}}}

        return response
    elif request_namespace == 'Alexa.Authorization':

        if request_name == 'AcceptGrant':
            response = {'event': {'header': {
                'namespace': 'Alexa.Authorization',
                'name': 'AcceptGrant.Response',
                'payloadVersion': '3',
                'messageId': '5f8a426e-01e4-4cc9-8b79-65f8bd0fd8a4',
            }, 'payload': {}}}

            return response
