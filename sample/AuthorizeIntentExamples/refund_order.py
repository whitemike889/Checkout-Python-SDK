from checkoutsdk.payments import CapturesRefundRequest
from sample import SampleSkeleton


class RefundOrder(SampleSkeleton):
    """Sample to Refund Order"""
    @staticmethod
    def build_request_body():
        """Method to build empty body"""
        return {}

    def refund_order(self, capture_id, debug=False):
        """Method to refund order using capture_id"""
        request = CapturesRefundRequest(capture_id)
        request.prefer("return=representation")
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code:', response.status_code
            print 'Status:', response.result.status
            print 'Order ID:', response.result.id
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        return response


if __name__ == "__main__":
    capture_id = '5GB86866A1365925K'
    RefundOrder().refund_order(capture_id, debug=True)
