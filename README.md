# REST API SDK for Python V2

![Home Image](homepage.jpg)

__Welcome to PayPal Python SDK__. This repository contains PayPal's Python SDK and samples for [v2/checkout/orders](https://developer.paypal.com/docs/api/orders/v2/) and [v2/payments](https://developer.paypal.com/docs/api/payments/v2/) APIs.

This is a part of the next major PayPal SDK. It includes a simplified interface to only provide simple model objects and blueprints for HTTP calls. This repo currently contains functionality for PayPal Checkout APIs which includes [Orders V2](https://developer.paypal.com/docs/api/orders/v2/) and [Payments V2](https://developer.paypal.com/docs/api/payments/v2/).

Please refer to the [PayPal Checkout Integration Guide](https://developer.paypal.com/docs/checkout/) for more information. Also refer to [Setup your SDK](https://developer.paypal.com/docs/checkout/reference/server-integration/setup-sdk/) for additional information about setting up the SDK's. 

## Prerequisites

Python 2.0+ or Python 3.0+

An environment which supports TLS 1.2 (see the TLS-update site for more information)

## Requirements

BraintreeHttp can be found at https://pypi.org/project/braintreehttp/

## Usage

### Binaries

It is not mandatory to fork this repository for using the PayPal SDK. You can refer [PayPal Checkout Server SDK](https://developer.paypal.com/docs/checkout/reference/server-integration) for configuring and working with SDK without forking this code.

For contirbuting or referrring the samples, You can fork/refer this repository. 

### Setting up credentials
Get client ID and client secret by going to https://developer.paypal.com/developer/applications and generating a REST API app. Get <b>Client ID</b> and <b>Secret</b> from there.

```python
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


# Creating Access Token for Sandbox
client_id = "<<PAYPAL-CLIENT-ID>>"
client_secret = "<<PAYPAL-CLIENT-SECRET>>"
# Creating an environment
environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(environment)
```

## Examples

### Creating an Order

#### Code:
```python
from paypalcheckoutsdk.orders import OrdersCreateRequest
from braintreehttp import HttpError
# Construct a request object and set desired parameters
# Here, OrdersCreateRequest() creates a POST request to /v2/checkout/orders
request = OrdersCreateRequest()

request.prefer('return=representation')

request.request_body (
    {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00"
                }
            }
        ]
    }
)

try:
    # Call API with your client and get a response for your call
    response = client.execute(request)
    print 'Order With Complete Payload:'
    print 'Status Code:', response.status_code
    print 'Status:', response.result.status
    print 'Order ID:', response.result.id
    print 'Intent:', response.result.intent
    print 'Links:'
    for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print 'Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
        response.result.purchase_units[0].amount.value)
        # If call returns body in response, you can get the deserialized version from the result attribute of the response
        order = response.result
        print order
except IOError as ioe:
    print ioe
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
```

#### Example Output:
```
Order With Complete Payload:
Status Code: 201
Status: CREATED
Order ID: 3MY95906MP2707106
Intent: CAPTURE
Links:
	self: https://api.sandbox.paypal.com/v2/checkout/orders/3MY95906MP2707106	Call Type: GET
Total Amount: USD 100.00
<class 'braintreehttp.http_response.Result'>
	approve: https://www.sandbox.paypal.com/checkoutnow?token=3MY95906MP2707106	Call Type: GET
Total Amount: USD 100.00
<class 'braintreehttp.http_response.Result'>
	update: https://api.sandbox.paypal.com/v2/checkout/orders/3MY95906MP2707106	Call Type: PATCH
Total Amount: USD 100.00
<class 'braintreehttp.http_response.Result'>
	capture: https://api.sandbox.paypal.com/v2/checkout/orders/3MY95906MP2707106/capture	Call Type: POST
Total Amount: USD 100.00
<class 'braintreehttp.http_response.Result'>
```

### Capturing an Order
After approving order above using `approve` link

#### Code:
```python
from paypalcheckoutsdk.orders import OrdersCaptureRequest
# Here, OrdersCaptureRequest() creates a POST request to /v2/checkout/orders
# Replace APPROVED-ORDER-ID with the actual approved order id.
request = OrdersCaptureRequest("APPROVED-ORDER-ID")

try:
    # Call API with your client and get a response for your call
    response = client.execute(request)

    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    order = response.result.id
except IOError as ioe:
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers
	print ioe
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
	Email Address: test-buyer@live.com
	Name: test buyer
	Phone Number: 408-411-2134
```
## Running tests

To run integration tests using your client id and secret, clone this repository and run the following command:
```sh
$ pip install nose # if not already installed
$ PAYPAL_CLIENT_ID=your_client_id PAYPAL_CLIENT_SECRET=your_client_secret nosetests --exe
```

## Samples

You can start off by trying out [creating and capturing an order](/sample/CaptureIntentExamples/run_all.py)

To try out different samples for both create and authorize intent check [this link](/sample)

Note: Update the `paypal_client.py` with your sandbox client credentials or pass your client credentials as environment variable whie executing the samples.


## License
Code released under [SDK LICENSE](LICENSE)  
