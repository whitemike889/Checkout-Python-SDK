import json
from pythonrestsdk.orders import OrdersCreateRequest
from sample.skeleton import Skeleton
import os


class CreateWithoutRepresentation(Skeleton):
    @staticmethod
    def build_request_body():
        jsondata = """
        {
          "intent": "CAPTURE",
          "application_context": {
            "return_url": "https://www.google.com",
            "cancel_url": "https://www.google.com",
            "brand_name": "EXAMPLE INC",
            "locale": "en-US",
            "landing_page": "BILLING",
            "shipping_preference": "SET_PROVIDED_ADDRESS",
            "user_action": "CONTINUE"
          },
          "purchase_units": [
            {
              "reference_id": "PUHF",
              "description": "Sporting Goods",
             
              "custom_id": "CUST-HighFashions",
              "soft_descriptor": "HighFashions",
              "amount": {
                "currency_code": "USD",
                "value": "230.00",
                "breakdown": {
                  "item_total": {
                    "currency_code": "USD",
                    "value": "180.00"
                  },
                  "shipping": {
                    "currency_code": "USD",
                    "value": "20.00"
                  },
                  "handling": {
                    "currency_code": "USD",
                    "value": "10.00"
                  },
                  "tax_total": {
                    "currency_code": "USD",
                    "value": "20.00"
                  },
                  "gift_wrap": {
                    "currency_code": "USD",
                    "value": "10.00"
                  },
                  "shipping_discount": {
                    "currency_code": "USD",
                    "value": "10"
                  }
                }
              },
              "payee": {
                "email_address": "rpenmetsa-us@paypal.com"
              },
              "items": [
                {
                  "name": "T-Shirt",
                  "description": "Green XL",
                  "sku": "sku01",
                  "unit_amount": {
                    "currency_code": "USD",
                    "value": "90.00"
                  },
                  "tax": {
                    "currency_code": "USD",
                    "value": "10.00"
                  },
                  "quantity": "1",
                  "category": "PHYSICAL_GOODS"
                },
                {
                  "name": "Shoes",
                  "description": "Running, Size 10.5",
                  "sku": "sku02",
                  "unit_amount": {
                    "currency_code": "USD",
                    "value": "45.00"
                  },
                  "tax": {
                    "currency_code": "USD",
                    "value": "5.00"
                  },
                  "quantity": "2",
                  "category": "PHYSICAL_GOODS"
                }
              ],
              "shipping": {
                "method": "United States Postal Service",
                "address": {
                  "name": {
                    "give_name":"John",
                    "surname":"Doe"
                  },
                  "address_line_1": "123 Townsend St",
                  "address_line_2": "Floor 6",
                  "admin_area_2": "San Francisco",
                  "admin_area_1": "CA",
                  "postal_code": "94107",
                  "country_code": "US"
                }
              }
            }
          ]
        }"""
        return json.loads(jsondata)

    def create_order(self, debug=False):
        request = OrdersCreateRequest()
        request.authorization(os.environ.get('PAYPAL_AUTHENTICATION_TOKEN'))
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
    CreateWithoutRepresentation().create_order(debug=True)
