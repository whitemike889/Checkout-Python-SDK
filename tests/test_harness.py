import unittest
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class TestHarness(unittest.TestCase):

    def setUp(self):
        client_id = "<<PAYPAL-CLIENT-ID>>"
        client_secret = "<<PAYPAL-CLIENT-SECRET>>"
        self.environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
        self.client = PayPalHttpClient(self.environment)
