import time

from selenium.webdriver import Keys

from test.Profiles.ENTProfile import ENTProfile
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ObjectActions:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def click_object(driver, locator):
        WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator)).click()

    @staticmethod
    def click_using_javascript(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.presence_of_element_located(locator))
        driver.execute_script("arguments[0].click();", element)

    @staticmethod
    def set_text(driver, locator, text):
        ObjectActions.clear_text(driver, locator)
        WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator)).send_keys(text)

    @staticmethod
    def clear_text(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator))
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)

    @staticmethod
    def is_visible(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator))
        return bool(element)

    @staticmethod
    def get_text(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator))
        return element.text

    @staticmethod
    def get_textbox_value(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator))
        return element.get_attribute('value')

    @staticmethod
    def select_first_value_from_dropdown(driver, locator):
        select = Select(
            WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator)))
        select.select_by_index(1)

    @staticmethod
    def is_checked(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator))
        return element.is_selected()

    @staticmethod
    def select_value_by_index(driver, locator, index):
        select = Select(
            WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator)))
        select.select_by_index(index)

    @staticmethod
    def select_value_from_dropdown(driver, locator, value):
        select = Select(
            WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator)))
        select.select_by_visible_text(value)

    @staticmethod
    def get_selected_dropdown_value(driver, locator):
        select = Select(
            WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator)))
        text_value = select.first_selected_option
        return text_value.text

    @staticmethod
    def wait_for_element(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.visibility_of_element_located(locator))
        return bool(element)

    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.element_to_be_clickable(locator))
        return bool(element)

    @staticmethod
    def verify_element_is_present_or_not(driver, locator):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.presence_of_element_located(locator))
        return bool(element)

    @staticmethod
    def verify_element_is_not_present(driver, locator):
        element = WebDriverWait(driver, 15).until(ec.invisibility_of_element(locator))
        return bool(element)

    @staticmethod
    def find_element(driver, locator):
        element = driver.find_element(locator[0], locator[1])
        return element

    @staticmethod
    def switch_to_frame(driver, locator):
        WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(
            ec.frame_to_be_available_and_switch_to_it((By.ID, locator)))

    @staticmethod
    def switch_to_default_content(driver):
        driver.switch_to.default_content()

    @staticmethod
    def switch_to_parent_frame(driver):
        driver.switch_to_parent_frame()

    @staticmethod
    def wait_for_loading_to_stop(driver, locator):
        WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(
            ec.text_to_be_present_in_element_attribute(locator, 'style', 'display: none;'))

    @staticmethod
    def get_current_window_title(driver):
        var = driver.title
        return var

    @staticmethod
    def switch_to_window_title(driver, title):
        windows = driver.window_handles
        for window in windows:
            driver.switch_to.window(window)
            if driver.title == title:
                print('SWITCHED TO....' + driver.title)
                time.sleep(2)
                driver.maximize_window()
                break

    @staticmethod
    def switch_to_window_index(driver, index):
        windows = driver.window_handles
        driver.switch_to.window(windows[index])

    @staticmethod
    def close_window_title(driver, title):
        windows = driver.window_handles
        for window in windows:
            driver.switch_to.window(window)
            if driver.title == title:
                time.sleep(2)
                driver.close()
                break

    @staticmethod
    def get_attribute_value(driver, locator, attribute):
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    @staticmethod
    def hover_over(driver, locator):
        a = ActionChains(driver)
        element = WebDriverWait(driver, ENTProfile.MAX_TIMEOUT).until(ec.presence_of_element_located(locator))
        a.move_to_element(element).perform()
