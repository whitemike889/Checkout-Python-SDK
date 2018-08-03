import os

from pythonrestsdk.core import PythonRestSdkHttpClient, PythonRestSdkEnvironment
from paypal_authentication_token import PayPalAuthenticationToken


class Skeleton(object):
    def __init__(self):
        environment = PythonRestSdkEnvironment(os.environ["BASE_URL"])
        self.client = PythonRestSdkHttpClient(environment)

    def authToken(self):
        return PayPalAuthenticationToken(
            username='AVNCVvV9oQ7qee5O8OW4LSngEeU1dI7lJAGCk91E_bjrXF2LXB2TK2ICXQuGtpcYSqs4mz1BMNQWuso1',
            password='EDQzd81k-1z2thZw6typSPOTEjxC_QbJh6IithFQuXdRFc7BjVht5rQapPiTaFt5RC-HCa1ir6mi-H5l').obtain_token()

