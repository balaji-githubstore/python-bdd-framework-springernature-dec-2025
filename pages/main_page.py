from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage:
    def __init__(self,driver):
        self.__driver:WebDriver=driver