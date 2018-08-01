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
        # requests.forms
        response = requests.post(self.path, auth=HTTPBasicAuth(self.username, self.password), headers=self.headers, data=self.body)
        os.environ['PAYPAL_AUTHENTICATION_TOKEN'] = str(response.json()['access_token'])
        return response.json()


# if __name__ == '__main__':
#     oauth_token = PayPalOAuth(
#         username='AVNCVvV9oQ7qee5O8OW4LSngEeU1dI7lJAGCk91E_bjrXF2LXB2TK2ICXQuGtpcYSqs4mz1BMNQWuso1',
#         password='EDQzd81k-1z2thZw6typSPOTEjxC_QbJh6IithFQuXdRFc7BjVht5rQapPiTaFt5RC-HCa1ir6mi-H5l')\
#         .obtain_token()
#
#     print(os.environ['PAYPAL_AUTHENTICATION_TOKEN'])

