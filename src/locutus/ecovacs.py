from os import environ
import sucks

config = {
    'email': environ.get('EMAIL'),
    'password_hash': environ.get('PASSWORDHASH'),
    'device_id': environ.get('DEVICEID'),
    'country': environ.get('COUNTRY'),
    'continent': environ.get('CONTINENT'),
}

api = sucks.EcoVacsAPI(config['device_id'], config['email'], config['password_hash'],
                         config['country'], config['continent'])
my_vac = api.devices()[0]
vacbot = sucks.VacBot(api.uid, api.REALM, api.resource, api.user_access_token, my_vac, config['continent'])
vacbot.connect_and_wait_until_ready()

def start():
    vacbot.run(sucks.Clean())  # start cleaning

def stop():
    vacbot.run(sucks.Charge()) # return to the charger
