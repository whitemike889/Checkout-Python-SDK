import unittest
import json
from paymentspythonsdk.payments import RefundsGetRequest
from tests.test_harness import TestHarness

class RefundsGetTest(TestHarness):

    def testRefundsGetTest(self):
        request = RefundsGetRequest('0CtW0xQKdBJ19qHgP')

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
