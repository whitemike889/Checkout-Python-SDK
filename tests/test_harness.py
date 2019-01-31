import unittest
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class TestHarness(unittest.TestCase):

    def setUp(self):
        client_id = "AVNCVvV9oQ7qee5O8OW4LSngEeU1dI7lJAGCk91E_bjrXF2LXB2TK2ICXQuGtpcYSqs4mz1BMNQWuso1"
        client_secret = "EDQzd81k-1z2thZw6typSPOTEjxC_QbJh6IithFQuXdRFc7BjVht5rQapPiTaFt5RC-HCa1ir6mi-H5l"
        self.environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
        self.client = PayPalHttpClient(self.environment)
