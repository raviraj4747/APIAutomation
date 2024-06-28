import random
import string
import requests
from test.Utilities.CommonActions import CommonActions
from test.conftest import BaseTest
from test.Keywords.ENT.Login import TestLogIn
from test.Pages.LogInPage import LogInPage
from test.Profiles.ENTProfile import ENTProfile
from test.Utilities.TestObjectAction import ObjectActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

testcase_name = "C3931393"

class TestLogin:
    def test_C3931393(self):
        url = 'https://www.google.com'
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

# Create an instance of TestLogin
test_login = TestLogin()

# Call the test method
test_login.test_C3931393()
