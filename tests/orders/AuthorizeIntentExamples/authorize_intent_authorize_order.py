import unittest
import json
from pythonrestsdk.orders import OrdersAuthorizeRequest
import os
from tests.test_harness import TestHarness

class AuthorizeIntentAuthorizeOrder(TestHarness):
    def build_request_body(self):
        return json.loads('{}')
    def testOrdersAuthorizeTest(self):
        order_id = '68461143JU904713W'
        request = OrdersAuthorizeRequest(order_id)
        request.authorization(os.environ.get('PAYPAL_AUTHENTICATION_TOKEN'))
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        print(response.result)
        print 'Status Code: ', response.status_code
        print 'Status: ', response.result.status
        print 'Order ID: ', response.result.id
        print 'Authorization ID:', response.result.purchase_units[0].payments.authorizations[0].id
        print 'Capture ID:', response.result.purchase_units[0].payments.captures[0].id
        print 'Links:'
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print 'Authorization Links:'
        for link in response.result.purchase_units[0].payments.authorizations[0].links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print 'Capture Links:'
        for link in response.result.purchase_units[0].payments.captures[0].links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print "Buyer:"
        print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
                                                                           response.result.payer.name.given_name + " " + response.result.payer.name.surname,
                                                                           response.result.payer.phone.phone_number.national_number)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
