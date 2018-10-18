from checkoutsdk.core import PayPalHttpClient, SandboxEnvironment
import json
from collections import OrderedDict

class PayPalClient:
    def __init__(self):
        self.client_id = "AVNCVvV9oQ7qee5O8OW4LSngEeU1dI7lJAGCk91E_bjrXF2LXB2TK2ICXQuGtpcYSqs4mz1BMNQWuso1"
        self.client_secret = "EDQzd81k-1z2thZw6typSPOTEjxC_QbJh6IithFQuXdRFc7BjVht5rQapPiTaFt5RC-HCa1ir6mi-H5l"
        
        """Setting up and Returns PayPal SDK environment with PayPal Access credentials.
           For demo purpose, we are using SandboxEnvironment. In production this will be
           LiveEnvironment."""
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        
        """ Returns PayPal HTTP client instance with environment which has access
            credentials context. This can be used invoke PayPal API's provided the
            credentials have the access to do so. """
        self.client = PayPalHttpClient(self.environment)

    def pretty_print(self, json_data, pre=""):
        """
        Function to print all json data in an organized readable manner
        """
        if type(json_data) is not OrderedDict:
            json_data = json.loads(json_data, object_pairs_hook=OrderedDict)
        pretty = ""
        for i, j in json_data.items():
            pretty += "{}{}: ".format(pre, i.capitalize())
            if type(j) is OrderedDict:
                pretty += self.pretty_print(j, pre + "\t")
            elif type(j) is list:
                for k, l in enumerate(j):
                    pretty += "\n{}{}:\n".format(pre + "\t", k + 1)
                    pretty += self.pretty_print(l, pre + "\t\t")
            else:
                pretty += j + "\n"

        return pretty
