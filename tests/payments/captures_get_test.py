import unittest
import json
from paymentspythonsdk.payments import CapturesGetRequest
from tests.test_harness import TestHarness

class CapturesGetTest(TestHarness):

    def testCapturesGetTest(self):
        request = CapturesGetRequest('258NWZhHX 34 4')

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
