import requests

class TestLogin:

    def test_dummy_api(self):
        # Dummy API endpoint
        url = 'https://www.google.com'
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
