import requests
import xmltodict
from collections import OrderedDict

from .Error import *
from .Module.Domain import Domain

class Client(object):
    API_ENDPOINT = 'https://api.openprovider.eu'

    def __init__(self):
        self.api_endpoint = self.API_ENDPOINT
        self.api_username = ''
        self.api_hash = ''

        setattr(self, 'domains', Domain(self))

    def getApiEndpoint(self):
        return self.api_endpoint

    def setApiEndpoint(self, api_endpoint):
        self.api_endpoint = api_endpoint.strip().rstrip('/')

    def setApiUsername(self, username):
        username = username.strip()
        self.api_username = username

    def setApiHash(self, hash):
        hash = hash.strip()
        self.api_hash = hash

    def setApiPassword(self, password):
        raise Error('You should not use a password to connect to the OpenProvider API, instead use a hash.')

    def performRequest(self, command, **kwargs):
        if not self.api_username:
            raise Error('You have not set an API username. Please use setApiUsername() to set the API username.')
        if not self.api_hash:
            raise Error('You have not set an API hash. Please use setApiHash() to set the API hash.')

        api_dict = {
            'openXML': OrderedDict({'credentials': {
                'username': self.api_username,
                'hash': self.api_hash,
            }})
        }
        api_dict['openXML'].update(command)

        # Convert the api_dict into XML
        data = xmltodict.unparse(api_dict)

        # Make a request to the OpenProvider API
        response = requests.post(self.api_endpoint, data=data)

        try:
            result = xmltodict.parse(response.text)
        except Exception as e:
            raise Error('Unable to decode OpenProvider response: "{0}".'.format(response.text))

        if int(result['openXML']['reply']['code']) == 0:
            return result['openXML']['reply'].get('data', None)
        else:
            code = int(result['openXML']['reply']['code'])
            desc = result['openXML']['reply']['desc']
            data = result['openXML']['reply'].get('data', '')
            raise Error('Error executing OpenProvider API call: "{0}" ({1}) {2}.'.format(desc, code, data).strip())
