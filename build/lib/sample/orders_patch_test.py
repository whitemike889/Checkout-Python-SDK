import unittest
import json
from checkoutsdk.orders import OrdersPatchRequest
from tests.test_harness import TestHarness

# TODO do something about this
class OrdersPatchTest(TestHarness):
    def build_request_body(self):
        return json.loads('{"from":"yKIJvATBe2Qe","op":"rcdJqfIwLwYv9cQ","path":"xsYTDthPhaXzS0f6","value":{}}')

    def testOrdersPatchTest(self):
        request = OrdersPatchRequest('Nyp9saDH2AZIHB')
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
