### Tests for intent _AUTHORIZE_

1. To test creating an order:
    * With Representation: run `authorize_intent_create_with_representation.py`
    * Without Representation: run  `authorize_intent_create_without_representation.py`

2. To approve your order, copy **_approve_** link into your browser and follow the instructions. When you're redirected to a different website move on to step 3.

3. Copy the **_Order ID_** from the response after creating order and replace the ```order_id``` variable in `authorize_intent_capture_order.py` with and run the test to authorize the payment.

4. Copy the Authorization ID from the response and replace `authorization_id` variable in `authorization_intent_capture_order` with the authorization ID from response to capture the payment.
  