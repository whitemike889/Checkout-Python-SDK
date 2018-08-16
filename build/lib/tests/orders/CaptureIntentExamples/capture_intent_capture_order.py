import unittest
import os
from pythonrestsdk.orders import OrdersCaptureRequest
from tests.test_harness import TestHarness

class CaptureIntentCaptureTest(TestHarness):
    def testOrdersCaptureTest(self):
        order_id = '0Y879375GR9684828'
        request = OrdersCaptureRequest(order_id)
        request.authorization('Bearer ' + self.authToken)
        response = self.client.execute(request)
        print 'Status Code: ', response.status_code
        print 'Status: ', response.result.status
        print 'Order ID: ', response.result.id
        print 'Links: '
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print "Buyer:"
        print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
                                                                       response.result.payer.name.given_name + " " + response.result.payer.name.surname,
                                                                       response.result.payer.phone.phone_number.national_number)

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
