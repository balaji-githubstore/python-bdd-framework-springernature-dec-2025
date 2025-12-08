from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'user opens browser with OrangeHRM application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'user enter the username as "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.NAME, "username").send_keys(username)


@when(u'user enter the password as "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)


@when(u'user clicks on login')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()


@then(u'user should get access to dashboard with header as "{expected_value}"')
def step_impl(context, expected_value):
    actual_value = context.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Quick')]").text
    assert_that(expected_value).is_equal_to(actual_value)
