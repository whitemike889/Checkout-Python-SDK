import unittest
import json
from pythonrestsdk.orders import OrdersValidateRequest
from tests.test_harness import TestHarness

class OrdersValidateTest(TestHarness):
    def build_request_body(self):
        return json.loads('{"payment_source":{"card":{"billing_address":{"address_line_1":"tJuzNU7X9fq3","address_line_2":"U Bw0KBS615","admin_area_3":"XVLdyV036ds63Qp","admin_area_4":"Jt NIgD4xRDUSZvZVz","country_code":"FPArrFO8sA","address_details":{"building_name":"gvdHrW5YRz2gRM","delivery_service":"GcJXd5aqNEXhX6ca","street_name":"7R3GbORfPZu4 VM","street_number":"vUvDZ30hTftA4","street_type":"2UJ029ti5Ga9WUTr9","sub_building":"YpdzepPFhCgw6T"},"address_line_3":"ZFqsYB2JO7O","admin_area_1":"G0ywW qvg6wVY","admin_area_2":"Yg25gJMXAiFpHsEUw","postal_code":"RqdFTdtA3acJ"},"card_type":"K5a1piaQ09izHU","expiry":"QEMpAVrwQqVw74TQhd","id":"Y7vt177Yvdp0QHs6","last_digits":"sTJVu4q7qvZSd Kia","name":"wOOcJYLcabBO","number":"EbbwN7Ov a","security_code":"T5IGKK0LcsKV xI"},"token":{"id":"N2Z3qPUU6x43J5B","type":"Ivt319ItXM6D"}}}')

    def testOrdersValidateTest(self):
        request = OrdersValidateRequest('bKMf4HaJgdza0')
        request.pay_pal_client_metadata_id('DzIP24z1IvMsLib')
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        # Add your own checks here

if __name__ == "__main__":
    unittest.main()
