import os
from pythonrestsdk.orders import OrdersCaptureRequest
from sample.skeleton import Skeleton


class Capture(Skeleton):
    def capture_order(self, order_id, debug=False):
        request = OrdersCaptureRequest(order_id)
        request.authorization('Bearer ' + self.authToken())
        response = self.client.execute(request)
        if debug:
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
        return response


if __name__ == "__main__":
    order_id = ''
    Capture().capture_order(order_id, debug=True)
