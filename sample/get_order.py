
from checkoutsdk.orders import OrdersGetRequest
from sample import SampleSkeleton
from sample.CaptureIntentExamples.create_order import CreateOrder


class GetOrder(SampleSkeleton):
    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        response = self.client.execute(request)
        print 'Status Code: ', response.status_code
        print 'Status: ', response.result.status
        print 'Order ID: ', response.result.id
        print 'Intent: ', response.result.intent
        print 'Links:'
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print 'Gross Amount: {} {}'.format(response.result.gross_amount.currency_code,
                                           response.result.gross_amount.value)


if __name__ == '__main__':
    createResponse = CreateOrder().create_order()
    order = createResponse.result
    GetOrder().get_order(order.id)
