from json import dumps, loads

from locutus.handlers import ecovacs_handler

def test_ecovacs_handler():
    res = ecovacs_handler({
        "directive": {
            "header": {
                "namespace": "Alexa.Discovery",
                "name": "Discover",
                "payloadVersion": "3",
                "messageId": "1bd5d003-31b9-476f-ad03-71d471922820"
            },
            "payload": {
                "scope": {
                    "type": "BearerToken",
                    "token": "access-token-from-skill"
                }
            }
        }
    }, {})

    assert True
