### Tests for intent _CAPTURE_

1. To test creating an order:
    * With Representation: run `capture_intent_create_with_representation.py`
    * Without Representation: run  `capture_intent_create_without_representation.py`

2. To authorize your order, copy **_approve_** link into your browser and follow the instructions. When you're redirected to a different website move on to step 3.

3. Copy the **_Order ID_** from the response after creating order and replace the ```order_id``` variable in `capture_intent_capture_order.py` with and run the test to capture the order.
  