# Testing Azure Packages has some additional complication/reading required.
# Reference https://github.com/Azure/azure-sdk-for-python/wiki/Contributing-to-the-tests
# Pytest should be leveraged to test your project.

def test_output():
    result = b'\xc3\xa9'
    assert result == u"é"