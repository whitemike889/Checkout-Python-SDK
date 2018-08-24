from checkoutsdk.orders import OrdersPatchRequest, OrdersGetRequest
from sample import SampleSkeleton
from sample.AuthorizeIntentExamples import CreateWithRepresentation


class PatchOrder(SampleSkeleton):
    @staticmethod
    def build_request_body():
        """Method to created body for patch order -> list of patches"""
        return \
            [
                {
                    "op": "replace",
                    "path": "/intent",
                    "value": "CAPTURE"
                },
                {
                    "op": "replace",
                    "path": "/purchase_units/@reference_id=='PUHF'/amount",
                    "value": {
                        "currency_code": "USD",
                        "value": "200.00",
                        "breakdown": {
                            "item_total": {
                                "currency_code": "USD",
                                "value": "180.00"
                            },
                            "tax_total": {
                                "currency_code": "USD",
                                "value": "20.00"
                            }
                        }
                    }
                }
            ]

    def patch_order(self):
        """Method to patch order"""
        print 'Before PATCH:'
        response = CreateWithRepresentation().create_order(True)
        order = response.result

        request = OrdersPatchRequest(order.id)
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        response = self.client.execute(OrdersGetRequest(order.id))
        print '\nAfter PATCH (Changed Intent and Amount):'
        print 'Status Code: ', response.status_code
        print 'Status: ', response.result.status
        print 'Order ID: ', response.result.id
        print 'Intent: ', response.result.intent
        print 'Links:'
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print 'Gross Amount: {} {}'.format(response.result.gross_amount.currency_code,
                                           response.result.gross_amount.value)


if __name__ == "__main__":
    PatchOrder().patch_order()
