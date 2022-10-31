from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
    context.driver = webdriver.Chrome()


@when('open SauceLabs webpage')
def openHomePage(context):
    context.driver.get("https://www.saucedemo.com")


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.CLASS_NAME, "bot_column").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
