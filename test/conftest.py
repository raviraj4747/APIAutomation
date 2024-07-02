import time

import pytest
import datetime
import os
from selenium import webdriver
from selenium.common import WebDriverException
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def init_driver(request):
    service = Service(executable_path=r'/usr/lib/chromium/chromedriver')
    o = Options()
    o.binary_location = '/usr/bin/chromium-browser'
    o.add_argument('--headless')
    o.add_argument('--ignore-certificate-errors')
    o.add_argument('--disable-gpu')
    o.add_argument('--no-sandbox')
    o.add_argument("--disable-dev-shm-usage")
    #   o.add_argument('--window-size=3800x2160')
    o.add_argument('--window-size=1900x1080')
    #   o.add_argument('--window-size=1024x3000')
    #   o.add_argument('start-maximized"')
    #   o.add_argument("--disable-renderer-backgrounding")
    #   o.add_argument("--disable-background-timer-throttling")
    #   o.add_argument("--disable-backgrounding-occluded-windows")
    #   o.add_argument("--disable-client-side-phishing-detection")
    #   o.add_argument("--disable-crash-reporter")
    #   o.add_argument("--disable-oopr-debug-crash-dump")
    #   o.add_argument("--no-crash-upload")
    #   o.add_argument("--disable-extensions")
    #   o.add_argument("--disable-low-res-tiling")
    #   o.add_argument("--log-level=3")
    #   o.add_argument("--silent")
    #   o.page_load_strategy = 'none'
    driver = webdriver.Chrome(service=service, options=o)
    driver.get(ENTProfile.BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(ENTProfile.MAX_TIMEOUT)
    driver.set_page_load_timeout(ENTProfile.MAX_TIMEOUT)
    request.cls.driver = driver


@pytest.fixture(scope='class')
def init_driverGrid(request):
    from selenium import webdriver

    # Maximum time to wait for the Selenium node to become available
    max_wait_time = 180  # seconds
    wait_interval = 5     # seconds

    start_time = time.time()

    while time.time() - start_time < max_wait_time:
        try:
            # Attempt to initialize the WebDriver instance
            driver = webdriver.Remote(
                #command_executor="http://10.80.146.42:4444/wd/hub",
                command_executor="http://10.80.146.57:4444/wd/hub",
                options=webdriver.ChromeOptions()
            )
            driver.implicitly_wait(ENTProfile.MAX_TIMEOUT)
            driver.get(ENTProfile.BASE_URL)
            driver.maximize_window()
            request.cls.driver = driver
            yield
            driver.quit()
            return
        except WebDriverException:
            # If the node is not found, wait for a certain interval before retrying
            time.sleep(wait_interval)

    # If the maximum wait time is exceeded without finding the node, raise an exception
    raise Exception("Selenium Grid node not found within the specified timeout period.")


# push the latest code push inside

@pytest.mark.usefixtures("init_driver")
#@pytest.mark.usefixtures("init_driverGrid")
class BaseTest:
    pass
