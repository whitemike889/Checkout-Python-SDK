import unittest
import json
from paymentspythonrestsdk.payments import CapturesRefundRequest
from tests.test_harness import TestHarness

class CapturesRefundTest(TestHarness):
    def build_request_body(self):
        return json.loads('{"note_to_payer":"R2gafxscg XeJptTfcB","amount":{"currency_code":"cM CrzuB0u","value":"WIrezsrCbHs"},"invoice_id":"KNyegZzzWV5yLQZ7"}')

    def testCapturesRefundTest(self):
        request = CapturesRefundRequest('69CNdIFw2u9')
        request.pay_pal_request_id('6zp0qSwCcVBKTX1Zcvp')
        request.prefer('sSgWGpPrcpte3TH')
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
