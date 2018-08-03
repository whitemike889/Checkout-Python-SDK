import unittest
import json
from paymentspythonrestsdk.payments import AuthorizationsCaptureRequest
from tests.test_harness import TestHarness

class AuthorizationsCaptureTest(TestHarness):
    def build_request_body(self):
        return json.loads('{"final_capture":true,"invoice_id":" 5U 3Fp NKMhx","payment_instruction":{"disbursement_mode":"xhOz0pb1Bp PV6 cJ","platform_fees":{"amount":{"currency_code":"FSMAiMy6Up8w11bH","value":"XFvp1iJeLOVFU"},"payee":{"merchant_id":"RNFgpT3X35S6NQC5","email_address":"MSYiBwO5Phc70q47Q"}}},"amount":{"currency_code":"6U9auhTwOP","value":"NszONqTca4hztGDBdN"}}')

    def testAuthorizationsCaptureTest(self):
        request = AuthorizationsCaptureRequest('tZQ9fCRL0UCFJO')
        request.pay_pal_request_id('raysZICXedqXVqd')
        request.prefer('RXb5Ma9BVRIMMEPeRTc')
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
