import requests
from requests.auth import HTTPBasicAuth
import os

class PayPalAuthenticationToken(object):
    """
    Class to obtain PayPal authentication token
    """
    def __init__(self, username, password, api_type="SANDBOX"):
        self.api_type = api_type
        self.path = "https://api.sandbox.paypal.com/v1/oauth2/token"
        self.username = username
        self.password = password
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.body = [("grant_type", "client_credentials")]

    def obtain_token(self):
        response = requests.post(self.path, auth=HTTPBasicAuth(self.username, self.password), headers=self.headers, data=self.body)
        return str(response.json()['access_token'])
