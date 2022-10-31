from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open SauceDemo Homepage')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com")


@when('Enter username "{user}" and password "{password}"')
def step_impl(context, user, password):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(password)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('User must successfully login to Basepage')
def step_impl(context):
    try:
        logo = context.driver.find_element(By.CSS_SELECTOR, "div.peek")
    except:
        context.driver.close()
        assert False, "Test Failed!"
    if logo.is_displayed():
        context.driver.close()
        assert True, "Test Passed!"

