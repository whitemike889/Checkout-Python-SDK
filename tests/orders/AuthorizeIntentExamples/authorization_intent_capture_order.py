import unittest
import json
from pythonsdk.payments import AuthorizationsCaptureRequest
from tests.test_harness import TestHarness

class AuthorizationsCaptureTest(TestHarness):
    def build_request_body(self):
        # return json.loads('{"final_capture":true,"invoice_id":" 5U 3Fp NKMhx","payment_instruction":{"disbursement_mode":"xhOz0pb1Bp PV6 cJ","platform_fees":{"amount":{"currency_code":"FSMAiMy6Up8w11bH","value":"XFvp1iJeLOVFU"},"payee":{"merchant_id":"RNFgpT3X35S6NQC5","email_address":"MSYiBwO5Phc70q47Q"}}},"amount":{"currency_code":"6U9auhTwOP","value":"NszONqTca4hztGDBdN"}}')
        return json.loads('{}')
    def testAuthorizationsCaptureTest(self):
        authorization_id = 'tZQ9fCRL0UCFJO'
        request = AuthorizationsCaptureRequest(authorization_id)
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
