import unittest
import json
from paymentspythonsdk.payments import AuthorizationsVoidRequest
from tests.test_harness import TestHarness

class AuthorizationsVoidTest(TestHarness):

    def testAuthorizationsVoidTest(self):
        request = AuthorizationsVoidRequest('PG5vDXCBz75eI8KG')

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
