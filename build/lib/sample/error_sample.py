from checkoutsdk.core import SampleSkeleton
import json
from checkoutsdk.orders import OrdersCreateRequest
from braintreehttp.http_error import HttpError


class CreateError(SampleSkeleton):

    def create_error_1(self):
        """
        Body has no required parameters (intent, purchase_units)
        """
        body = """{}"""
        request = OrdersCreateRequest()
        request.authorization('Bearer ' + self.authToken())
        request.request_body(json.loads(body))
        print "Request Body:", body, "\n"
        print "Response:"
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print "Status Code:", h.status_code
            print self.pretty_print(h.message)

    def create_error_2(self):
        """
        Authorization header has an empty string
        """
        body = """\n{\n\t"intent": "CAPTURE",\n\t"purchase_units": [\n\t\t{"amount": \n\t\t\t{\n\t\t\t\t"currency_code": "USD",\n\t\t\t\t"value": "100.00"\n\t\t\t}\n\t\t}\n\t]\n}"""
        print "Request Body:", body, "\n"
        request = OrdersCreateRequest()
        request.authorization("")
        request.request_body(json.loads(body))
        print "Response:"
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print "Status Code: ", h.status_code
            print self.pretty_print(h.message)

    def create_error_3(self):
        """
        Body has invalid parameter value for intent
        """
        body = """\n{\n\t"intent": "INVALID",\n\t"purchase_units": [\n\t\t{"amount": \n\t\t\t{\n\t\t\t\t"currency_code": "USD",\n\t\t\t\t"value": "100.00"\n\t\t\t}\n\t\t}\n\t]\n}"""
        request = OrdersCreateRequest()
        request.authorization('Bearer ' + self.authToken())
        request.request_body(json.loads(body))
        print "Request Body:", body, "\n"
        print "Response:"
        response = ""
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print "Status Code: ", h.status_code
            print self.pretty_print(h.message)

print "Calling create_error_1 (Body has no required parameters (intent, purchase_units))"
CreateError().create_error_1()

print "\nCalling create_error_2 (Authorization header has an empty string)"
CreateError().create_error_2()

print "\nExecuting create_error_3 (Body has invalid parameter value for intent)"
CreateError().create_error_3()
