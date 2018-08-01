import unittest
import json
from pythonsdk.orders import OrdersGetRequest
from tests.test_harness import TestHarness

class OrdersGetTest(TestHarness):

    def testOrdersGetTest(self):
        request = OrdersGetRequest('zGb0RWXRdgYPq85')

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
