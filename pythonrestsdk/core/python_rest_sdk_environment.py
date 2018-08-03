import braintreehttp

class PythonRestSdkEnvironment(braintreehttp.Environment):

    def base_url(self):
        # braintreehttp.Environment.__init__(self, YOUR_API_BASE_URL)
        raise NotImplementedError()
