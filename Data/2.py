import random
import string
from test.Utilities.CommonActions import CommonActions
from test.conftest import BaseTest
from test.Keywords.ENT.Login import TestLogIn
from test.Profiles.ENTProfile import ENTProfile
from test.Utilities.TestObjectAction import ObjectActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

testcase_name = "C3931393"


class TestCreatePatient(BaseTest):

    def test_C3931393(self):

        try:
            # login into application
            TestLogIn.login_into_application(self.driver, ENTProfile.USERNAME15, ENTProfile.PASSWORD)
            time.sleep(60)
            # create patient
            # Navigate to create patient page

        except:
            CommonActions.mark_fail(self.driver, testcase_name)

        else:
            CommonActions.mark_pass(self.driver, testcase_name)
