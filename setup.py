import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="paypalcheckoutsdk",
    version="0.0.5",
    author="Ganeshram Chockalingam",
    author_email="ganeshramc@live.com",
    description="Python Rest SDK for PayPal Checkout",
    long_description="Python Rest SDK for PayPal Checkout",
    long_description_content_type="text/markdown",
    url="https://github.paypal.com/gchockalingam/Checkout-python-SDK/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)