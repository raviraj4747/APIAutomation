import random
import string
import threading

from test.Utilities.PageNavigations import PageNavigations
from test.Utilities.CommonActions import CommonActions
from test.conftest import BaseTest
from test.Keywords.ENT.Login import TestLogIn
from test.Profiles.ENTProfile import ENTProfile
from test.Pages.ENT.HomePage import HomePage
from test.Utilities.TestObjectAction import ObjectActions
import time

testcase_name = "10001"


class TestPageLoad(BaseTest):

    def test_case1(self):

        try:
            lock = threading.Lock()
            # login into application
            TestLogIn.login_into_application(self.driver, ENTProfile.USERNAME1, ENTProfile.PASSWORD)

            page_load = PageNavigations.func1(self.driver)

            with lock:
                with open(r"stat1.txt", "a") as statsfile:
                    statsfile.write(page_load)

        except:
            CommonActions.mark_fail(self.driver, testcase_name)

        else:
            CommonActions.mark_pass(self.driver, testcase_name)
