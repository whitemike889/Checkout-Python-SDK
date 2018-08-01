import unittest
import json
from paymentspythonsdk.payments import AuthorizationsGetRequest
from tests.test_harness import TestHarness

class AuthorizationsGetTest(TestHarness):

    def testAuthorizationsGetTest(self):
        request = AuthorizationsGetRequest('eJQOFqSOYW')

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
