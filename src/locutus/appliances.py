def get_endpoint_from_v3_appliance(appliance):
    endpoint = {
        'endpointId': appliance['applianceId'],
        'manufacturerName': appliance['manufacturerName'],
        'friendlyName': appliance['friendlyName'],
        'description': appliance['friendlyDescription'],
        'displayCategories': [],
        'cookie': appliance['additionalApplianceDetails'],
        'capabilities': [],
    }
    endpoint['displayCategories'] = \
        get_display_categories_from_v3_appliance(appliance)
    endpoint['capabilities'] = \
        get_capabilities_from_v3_appliance(appliance)
    return endpoint


def get_display_categories_from_v3_appliance(appliance):
    model_name = appliance['modelName']
    if model_name == 'Smart Switch':
        displayCategories = ['SWITCH']
    elif model_name == 'Smart Light':
        displayCategories = ['LIGHT']
    elif model_name == 'Smart White Light':
        displayCategories = ['LIGHT']
    elif model_name == 'Smart Thermostat':
        displayCategories = ['THERMOSTAT']
    elif model_name == 'Smart Lock':
        displayCategories = ['SMARTLOCK']
    elif model_name == 'Smart Scene':
        displayCategories = ['SCENE_TRIGGER']
    elif model_name == 'Smart Activity':
        displayCategories = ['ACTIVITY_TRIGGER']
    elif model_name == 'Smart Camera':
        displayCategories = ['CAMERA']
    else:
        displayCategories = ['OTHER']
    return displayCategories


def get_capabilities_from_v3_appliance(appliance):
    model_name = appliance['modelName']
    if model_name == 'Smart Switch':
        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.PowerController',
            'version': '3',
            'properties': {'supported': [{'name': 'powerState'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }]
    elif model_name == 'Smart Light':

        capabilities = [
            {
                'type': 'AlexaInterface',
                'interface': 'Alexa.PowerController',
                'version': '3',
                'properties': {'supported': [{'name': 'powerState'}],
                               'proactivelyReported': True,
                               'retrievable': True},
            },
            {
                'type': 'AlexaInterface',
                'interface': 'Alexa.ColorController',
                'version': '3',
                'properties': {'supported': [{'name': 'color'}],
                               'proactivelyReported': True,
                               'retrievable': True},
            },
            {
                'type': 'AlexaInterface',
                'interface': 'Alexa.ColorTemperatureController',
                'version': '3',
                'properties': {'supported': [{'name': 'colorTemperatureInKelvin'
                                              }], 'proactivelyReported': True,
                               'retrievable': True},
            },
            {
                'type': 'AlexaInterface',
                'interface': 'Alexa.BrightnessController',
                'version': '3',
                'properties': {'supported': [{'name': 'brightness'}],
                               'proactivelyReported': True,
                               'retrievable': True},
            },
            {
                'type': 'AlexaInterface',
                'interface': 'Alexa.PowerLevelController',
                'version': '3',
                'properties': {'supported': [{'name': 'powerLevel'}],
                               'proactivelyReported': True,
                               'retrievable': True},
            },
            {
                'type': 'AlexaInterface',
                'interface': 'Alexa.PercentageController',
                'version': '3',
                'properties': {'supported': [{'name': 'percentage'}],
                               'proactivelyReported': True,
                               'retrievable': True},
            },
        ]
    elif model_name == 'Smart White Light':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.PowerController',
            'version': '3',
            'properties': {'supported': [{'name': 'powerState'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }, {
            'type': 'AlexaInterface',
            'interface': 'Alexa.ColorTemperatureController',
            'version': '3',
            'properties': {'supported': [{'name': 'colorTemperatureInKelvin'
                                          }], 'proactivelyReported': True,
                           'retrievable': True},
        }, {
            'type': 'AlexaInterface',
            'interface': 'Alexa.BrightnessController',
            'version': '3',
            'properties': {'supported': [{'name': 'brightness'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }, {
            'type': 'AlexaInterface',
            'interface': 'Alexa.PowerLevelController',
            'version': '3',
            'properties': {'supported': [{'name': 'powerLevel'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }, {
            'type': 'AlexaInterface',
            'interface': 'Alexa.PercentageController',
            'version': '3',
            'properties': {'supported': [{'name': 'percentage'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }]
    elif model_name == 'Smart Thermostat':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.ThermostatController',
            'version': '3',
            'properties': {'supported': [{'name': 'targetSetpoint'},
                                         {'name': 'thermostatMode'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }, {
            'type': 'AlexaInterface',
            'interface': 'Alexa.TemperatureSensor',
            'version': '3',
            'properties': {'supported': [{'name': 'temperature'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }]
    elif model_name == 'Smart Thermostat Dual':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.ThermostatController',
            'version': '3',
            'properties': {'supported': [{'name': 'upperSetpoint'},
                                         {'name': 'lowerSetpoint'},
                                         {'name': 'thermostatMode'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }, {
            'type': 'AlexaInterface',
            'interface': 'Alexa.TemperatureSensor',
            'version': '3',
            'properties': {'supported': [{'name': 'temperature'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }]
    elif model_name == 'Smart Lock':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.LockController',
            'version': '3',
            'properties': {'supported': [{'name': 'lockState'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }]
    elif model_name == 'Smart Scene':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.SceneController',
            'version': '3',
            'supportsDeactivation': False,
            'proactivelyReported': True,
        }]
    elif model_name == 'Smart Activity':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.SceneController',
            'version': '3',
            'supportsDeactivation': True,
            'proactivelyReported': True,
        }]
    elif model_name == 'Smart Camera':

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.CameraStreamController',
            'version': '3',
            'cameraStreamConfigurations': [{
                'protocols': ['RTSP'],
                'resolutions': [{'width': 1280, 'height': 720}],
                'authorizationTypes': ['NONE'],
                'videoCodecs': ['H264'],
                'audioCodecs': ['AAC'],
            }],
        }]
    else:

        # in this example, just return simple on/off capability

        capabilities = [{
            'type': 'AlexaInterface',
            'interface': 'Alexa.PowerController',
            'version': '3',
            'properties': {'supported': [{'name': 'powerState'}],
                           'proactivelyReported': True,
                           'retrievable': True},
        }]

    # additional capabilities that are required for each endpoint

    endpoint_health_capability = {
        'type': 'AlexaInterface',
        'interface': 'Alexa.EndpointHealth',
        'version': '3',
        'properties': {'supported': [{'name': 'connectivity'}],
                       'proactivelyReported': True,
                       'retrievable': True},
    }

    alexa_interface_capability = {'type': 'AlexaInterface',
                                  'interface': 'Alexa', 'version': '3'}
    capabilities.append(endpoint_health_capability)
    capabilities.append(alexa_interface_capability)
    return capabilities
