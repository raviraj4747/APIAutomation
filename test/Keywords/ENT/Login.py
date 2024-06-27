import time

from test.Pages.LogInPage import LogInPage
from test.Utilities.TestObjectAction import ObjectActions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from test.Profiles.ENTProfile import ENTProfile


class TestLogIn:

    @staticmethod
    def login_into_application(driver, username, password):
        print("Hello")

    # Enter Username and Password
    #   ObjectActions.set_text(driver, LogInPage.USERNAME, username)
    #   ObjectActions.set_text(driver, LogInPage.PASSWORD, password)

    # Click on Login Button
    #   ObjectActions.click_object(driver, LogInPage.LOGIN_BUTTON)

    # ObjectActions.wait_for_element_to_be_clickable(driver, HomePage.HOME)
    #
    # time.sleep(5)
    # notifi = ObjectActions.verify_element_is_not_present(driver, HomePage.BUTTON_SAVE_AS_READ)
    # if not notifi:
    #     while not notifi:
    #         ObjectActions.click_object(driver, HomePage.BUTTON_SAVE_AS_READ)
    #         ObjectActions.verify_element_is_not_present(driver, HomePage.BUTTON_SAVE_AS_READ)
    #
    #   while len(driver.find_elements(HomePage.BUTTON_SAVE_AS_READ[0],
    #                                 HomePage.BUTTON_SAVE_AS_READ[1])) != 0:
    #      driver.find_element(HomePage.BUTTON_SAVE_AS_READ[0],
    #                          HomePage.BUTTON_SAVE_AS_READ[1]).click()
    #      time.sleep(5)

    #  ObjectActions.wait_for_element_to_be_clickable(driver, HomePage.HOME)

