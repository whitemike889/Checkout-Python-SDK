### Sample Execution for intent _CAPTURE_

This can be performed by either doing running `run_all.py` or by following the instructions below

1. To test creating an order, run `create_order.py`

2. To authorize your order, copy **_approve_** link into your browser and follow the instructions. When you're redirected to a different website move on to step 3.

3. Copy the **_Order ID_** from the response after creating order and replace the ```order_id``` variable in `capture_order.py` with and run the test to capture the order.
  