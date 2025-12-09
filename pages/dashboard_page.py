from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.__driver = driver

    def get_quick_launch_text(self):
        return self.__driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Quick')]").text
