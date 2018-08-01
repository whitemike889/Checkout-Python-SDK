import braintreehttp

class PythonSdkHttpClient(braintreehttp.HttpClient):

    def __init__(self, environment):
        braintreehttp.HttpClient.__init__(self, environment)

    def get_user_agent(self):
        return "PythonSdk HttpClient"

