import braintreehttp

class PythonRestSdkEnvironment(braintreehttp.Environment):

    def base_url(self, base_url):
        braintreehttp.Environment.__init__(self, base_url)
