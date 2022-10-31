from behave import *
from selenium.webdriver.common.by import By


@when('I click the logout button')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()


@when('I add to cart a product')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()


@then('I must be on the homepage')
def step_impl(context):
    try:
        robotImg = context.driver.find_element(By.CSS_SELECTOR, "div.bot_column")
    except:
        context.driver.close()
        assert False, "Logout Test Failed!"
    if robotImg.is_displayed():
        context.driver.close()
        assert True, "Logout Test Passed!"


@then('Product must appear on my cart')
def step_impl(context):
    try:
        product_name = context.driver.find_element(By.CSS_SELECTOR, "div.inventory_item_name").text
    except:
        context.driver.close()
        assert False, "Product Cart Test Failed!"
    if product_name == "Sauce Labs Backpack":
        context.driver.close()
        assert True, "Product Cart Test Passed!"
