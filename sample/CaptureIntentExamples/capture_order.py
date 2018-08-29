from checkoutsdk.orders import OrdersCaptureRequest
from sample import SampleSkeleton


class CaptureOrder(SampleSkeleton):
    """Sample to Capture Order"""
    def capture_order(self, order_id, debug=False):
        """Method to capture order using order_id"""
        request = OrdersCaptureRequest(order_id)
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
    CaptureOrder().capture_order(order_id, debug=True)
