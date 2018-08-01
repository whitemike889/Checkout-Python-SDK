import unittest
import json
from paymentspythonsdk.payments import AuthorizationsReauthorizeRequest
from tests.test_harness import TestHarness

class AuthorizationsReauthorizeTest(TestHarness):
    def build_request_body(self):
        return json.loads('{"amount":{"currency_code":"  W6UCVuKa","value":"CQHaYThINxg"}}')

    def testAuthorizationsReauthorizeTest(self):
        request = AuthorizationsReauthorizeRequest('rwsGMN3VvO')
        request.pay_pal_request_id('aa1xp9O5dcD')
        request.prefer('4tg dI6gw51xQSA4CW')
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
