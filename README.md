# PayPal SDK V2

This is a part of the next major PayPal SDK. It includes a simplified interface to only provide simple model objects and blueprints for HTTP calls. This repo currently contains functionality for PayPal Checkout APIs which includes Orders V2 and Payments V2.

## Creating an Order

```python
from pythonrestsdk.core import PythonRestSdkHttpClient, PythonRestSdkEnvironment, PayPalAuthenticationToken
from pythonrestsdk.orders import OrdersCreateRequest

# Creating Access Token for Sandbox
clientId = "AVNCVvV9oQ7qee5O8OW4LSngEeU1dI7lJAGCk91E_bjrXF2LXB2TK2ICXQuGtpcYSqs4mz1BMNQWuso1";
clientSecret = "EDQzd81k-1z2thZw6typSPOTEjxC_QbJh6IithFQuXdRFc7BjVht5rQapPiTaFt5RC-HCa1ir6mi-H5l";
authToken = PayPalAuthenticationToken().createAuthToken(clientId, clientSecret);

# Creating an environment
environment = PythonRestSdkEnvironment(os.environ["BASE_URL"])
client = PythonRestSdkHttpClient(environment)

# Construct a request object and set desired parameters
# Here, OrdersCreateRequest() creates a POST request to /v2/checkout/orders
request = OrdersCreateRequest()
request.authorization('Bearer ' + authToken)
request.request_body = (json.loads("{
                                        "intent": "CAPTURE",
                                        "purchase_units": [
                                            {
                                                "amount": {
                                                    "currency_code": "USD",
                                                    "value": "100.00"
                                                }
                                            }
                                        ]
                                    }"))

try:
    # Call API with your client and get a response for your call
    response = client.execute(request);  
    
    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    order = response.result;
except IOError as ioe:
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers["debug_id"]
    else:
        # Something went wrong client side
        print ioe
```


## Capturing an Order

```python
# Here, OrdersCaptureRequest() creates a POST request to /v2/checkout/orders
# order.id gives the orderId of the order created above
request = OrdersCaptureRequest(order.id).authToken('Bearer ' + authToken);

try:
    # Call API with your client and get a response for your call
    response = client.execute(request);  
    
    # If call returns body in response, you can get the deserialized version from the result attribute of the response
    order = response.result;
except IOError as ioe:
    if isinstance(ioe, HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers["debug_id"]
    else:
        # Something went wrong client side
        print ioe
```
## Samples

You can start off by trying out [creating and capturing an order](/sample/CaptureIntentExamples/run_all.py)

To try out different samples for both create and authorize intent check [this link](/sample)
