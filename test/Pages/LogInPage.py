from selenium.webdriver.common.by import By


class LogInPage:
    USERNAME = (By.XPATH, '//*[@id="Username"]')
    PASSWORD = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/input[3]')
    LOGIN_BUTTON2 = (By.XPATH, '//*[@id="login"]/button')

    SELECT_CLOUD = (By.XPATH, "//*[@id='SelectedPortal']")
    Click_image = (By.XPATH, "//*[@id='Masthead454']/div[1]/ul/li[3]/a/p/span[1]")
    Click_image1 = (By.XPATH, "//*[@id='Masthead454']/div[1]/ul/li[3]/a/p3535/span[979798]")
    Contact_us = (By.XPATH, "//*[@id='pagetop']/header/div/nav/ul[1]/li[2]/a/span")
    Contact_group_holding = (By.XPATH, "//*[@id='pagetop']/main/div/div[1]/ul/li/a/span")
    Contact_feedback = (By.XPATH, "//*[@id='01']/ul/li[1]/div/a")
