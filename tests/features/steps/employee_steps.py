import time
import random
from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when(u'user clicks on PIM menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='PIM']").click()


@when(u'user clicks on Add Employee')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()


@when(u'user fill the employee details form')
def step_impl(context):
    # storing the datatable of employee under employee_table variable name
    context.employee_table=context.table
    context.driver.find_element(By.NAME, "firstName").send_keys(context.table.rows[0]["firstName"])
    context.driver.find_element(By.NAME, "middleName").send_keys(context.table.rows[0]["middleName"])
    context.driver.find_element(By.NAME, "lastName").send_keys(context.table.rows[0]["lastName"])
#
    context.driver.find_element(By.XPATH, "//label[text()='Employee Id']/following::input").send_keys(context.table.rows[0]["employeeId"])
    # str(int(random.random() * 1000))
    # context.driver.find_element(By.XPATH, "//label[text()='Employee Id']/following::input").send_keys(
    #     str(int(random.random() * 1000)))

@when(u'user clicks on save employee')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Save')]").click()


@then(u'user should get the profile name as "{expected_profile_name}"')
def step_impl(context, expected_profile_name):
    actual_value = context.driver.find_element(By.XPATH,
                                               f"//h6[contains(normalize-space(),'{expected_profile_name}')]").text
    assert_that(expected_profile_name).is_equal_to(actual_value)


@then(u'user should get the firstname field as "{expected_first_name}"')
def step_impl(context, expected_first_name):
    actual_first_name = context.driver.find_element(By.XPATH, "//input[@name='firstName']").get_attribute("value")
    assert_that(expected_first_name).is_equal_to(actual_first_name)


@then(u'user should get the same form details in the personal detail page')
def step_impl(context):
     dt= context.employee_table
     print(dt.rows[0]["firstName"])
     print(str(context.username))

