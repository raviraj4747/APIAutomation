import requests

def test_dummy_api():
    # Dummy API endpoint
    url = 'https://www.google.com'
    response = requests.get(url)
    assert response.status_code == 200

if __name__ == '__main__':
    test_dummy_api()
