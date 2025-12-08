"""Environment file with behave hooks, etc."""
from selenium import webdriver



def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()

