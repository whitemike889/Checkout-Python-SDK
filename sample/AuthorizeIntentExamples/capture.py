import json
import os
from pythonrestsdk.payments import AuthorizationsCaptureRequest
from sample.skeleton import Skeleton


class Capture(Skeleton):
    @staticmethod
    def build_request_body():
        return json.loads('{}')

    def capture_order(self, authorization_id, debug=False):
        request = AuthorizationsCaptureRequest(authorization_id)
        request.authorization('Bearer ' + self.authToken())
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Order ID: ', response.result.id
            print 'Links: '
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        return response


if __name__ == "__main__":
    auth_id = '0LC80782T3164811U'
    Capture().capture_order(auth_id, debug=True)
