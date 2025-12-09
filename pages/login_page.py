from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver: WebDriver = driver
        self.__username_locator = (By.NAME, "username")
        self.__password_locator = (By.NAME, "password")
        self.__login_locator = (By.XPATH, "//button[contains(normalize-space(),'Login')]")
        self.__error_locator = (By.XPATH, "//p[contains(normalize-space(),'Invalid')]")
        self.__header_locator = (By.XPATH, "//h5[text()='Login']")

    def enter_username(self, username):
        self.type_on_element(locator=self.__username_locator, text=username)

    def enter_password(self, password):
        self.type_on_element(locator=self.__password_locator, text=password)

    def click_on_login(self):
        self.click_on_element(self.__login_locator)

    def get_invalid_error_message(self):
        return self.get_text_from_element(self.__error_locator)

    def get_login_header(self):
        return self.get_text_from_element(self.__header_locator)

    def get_username_placeholder(self):
        return self.get_attribute_from_element(locator=self.__username_locator, attribute_name="placeholder")

    def get_password_placeholder(self):
        return self.get_attribute_from_element(self.__password_locator, "placeholder")
