import braintreehttp

class PythonRestSdkHttpClient(braintreehttp.HttpClient):

    def __init__(self, environment):
        braintreehttp.HttpClient.__init__(self, environment)

    def get_user_agent(self):
        return "PythonRestSdk HttpClient"

