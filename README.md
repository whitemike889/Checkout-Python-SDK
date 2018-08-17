# REST API SDK for Python V2

![Home Image](homepage.jpg)

__Welcome to PayPal Python SDK__. This repository contains PayPal's Python SDK and samples for REST API.

This is a part of the next major PayPal SDK. It includes a simplified interface to only provide simple model objects and blueprints for HTTP calls. This repo currently contains functionality for PayPal Checkout APIs which includes Orders V2 and Payments V2.

## Prerequisites

Python 2.0+ or Python 3.0+

An environment which supports TLS 1.2 (see the TLS-update site for more information)

## Usage

### Setting up credentials
Get client ID and client secret by going to https://developer.paypal.com/developer/applications and generating a REST API app. Get <b>Client ID</b> and <b>Secret</b> from there.

```python
from pythonrestsdk.core import PythonRestSdkHttpClient, PythonRestSdkEnvironment, PayPalAuthenticationToken, Skeleton


# Creating Access Token for Sandbox
clientId = "AVNCVvV9oQ7qee5O8OW4LSngEeU1dI7lJAGCk91E_bjrXF2LXB2TK2ICXQuGtpcYSqs4mz1BMNQWuso1"
clientSecret = "EDQzd81k-1z2thZw6typSPOTEjxC_QbJh6IithFQuXdRFc7BjVht5rQapPiTaFt5RC-HCa1ir6mi-H5l"
authToken = PayPalAuthenticationToken(clientId, clientSecret).obtain_token()

# Creating an environment
client = Skeleton().client
```

## Examples

### Creating an Order

#### Code: 
```python
from pythonrestsdk.orders import OrdersCreateRequest
# Construct a request object and set desired parameters
# Here, OrdersCreateRequest() creates a POST request to /v2/checkout/orders
request = OrdersCreateRequest()
request.authorization('Bearer ' + authToken)
request.request_body = ({
                            "intent": "CAPTURE",
                            "purchase_units": [
                                {
                                    "amount": {
                                        "currency_code": "USD",
                                        "value": "100.00"
                                    }
                                }
                            ]
                        })

try:
    # Call API with your client and get a response for your call
    response = client.execute(request) 
    
    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    order = response.result
    print response.result
except IOError as ioe:
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers["debug_id"]
    else:
        # Something went wrong client side
        print ioe
```

#### Example Output:
```
Status Code:  201
Status:  CREATED
Order ID:  7F845507FB875171H
Intent:  AUTHORIZE
Links:
	self: https://api.sandbox.paypal.com/v2/checkout/orders/7F845507FB875171H	Call Type: GET
	approve: https://www.sandbox.paypal.com/checkoutnow?token=7F845507FB875171H	Call Type: GET
	authorize: https://api.sandbox.paypal.com/v2/checkout/orders/7F845507FB875171H/authorize	Call Type: POST
Gross Amount: USD 230.00
```

### Capturing an Order

#### Code:
```python
from pythonrestsdk.orders import OrdersCaptureRequest
# Here, OrdersCaptureRequest() creates a POST request to /v2/checkout/orders
# order.id gives the orderId of the order created above
request = OrdersCaptureRequest(order.id).authToken('Bearer ' + authToken)

try:
    # Call API with your client and get a response for your call
    response = client.execute(request)
    
    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    order = response.result
except IOError as ioe:
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers["debug_id"]
    else:
        # Something went wrong client side
        print ioe
```

#### Example Output:
```
Status Code:  201
Status:  COMPLETED
Order ID:  7F845507FB875171H
Links: 
	self: https://api.sandbox.paypal.com/v2/checkout/orders/70779998U8897342J	Call Type: GET
Buyer:
	Email Address: ganeshramc-buyer@live.com
	Name: test buyer
	Phone Number: 408-411-2134
```
## Samples

You can start off by trying out [creating and capturing an order](/sample/CaptureIntentExamples/run_all.py)

To try out different samples for both create and authorize intent check [this link](/sample)
