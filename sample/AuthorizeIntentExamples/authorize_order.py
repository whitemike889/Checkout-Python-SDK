from checkoutsdk.orders import OrdersAuthorizeRequest
from sample import SampleSkeleton


class AuthorizeOrder(SampleSkeleton):
    """Sample to Authorize Order"""
    @staticmethod
    def build_request_body():
        """Method to build empty body"""
        return {}

    def authorize_order(self, order_id, debug=False):
        """Method to authorize order using order_id"""
        request = OrdersAuthorizeRequest(order_id)
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Order ID: ', response.result.id
            print 'Authorization ID:', response.result.purchase_units[0].payments.authorizations[0].id
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print 'Authorization Links:'
            for link in response.result.purchase_units[0].payments.authorizations[0].links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print "Buyer:"
            print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
                                                                               response.result.payer.name.given_name + " " + response.result.payer.name.surname,
                                                                               response.result.payer.phone.phone_number.national_number)
        return response


if __name__ == "__main__":
    order_id = '1AL141024Y8279459'
    Authorize().authorize_order(order_id, debug=True)
