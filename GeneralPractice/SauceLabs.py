import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options = chrome_options
)

wait = WebDriverWait(driver, 20)
class SauceLabs():
    def cart(self):
        driver.get("https://www.saucedemo.com/v1/")
        driver.maximize_window()

        username = wait.until(element_to_be_clickable((By.ID, "user-name")))
        username.click()
        username.send_keys("standard_user")

        Action = ActionChains(driver)
        Action.send_keys(Keys.TAB).perform()
        Action.send_keys("secret_sauce").perform()

        driver.find_element(By.ID, "login-button").click()


        time.sleep(2)

        dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()

        select =Select(dropdown)
        select.select_by_visible_text("Price (high to low)")
        # select.click()
        time.sleep(3)

        #ancestor use
        driver.find_element(
            By.XPATH,
            "//div[contains(text(),'not every day that you come across a midweight')]/ancestor::div[@class='inventory_item']//button[@class='btn_primary btn_inventory']"
        ).click()

        driver.find_element(
            By.XPATH,
            "//div[contains(text(),'uncompromising style with unequaled laptop and tablet protection')]/ancestor::div[@class='inventory_item']//button[@class='btn_primary btn_inventory']"
        ).click()

        driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()

        time.sleep(3)

        first_name = driver.find_element(By.ID, "first-name")
        first_name.click()
        first_name.send_keys("Test")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.click()
        last_name.send_keys("User")

        zip = driver.find_element(By.ID, "postal-code")
        zip.click()
        zip.send_keys("12345")

        driver.find_element(By.XPATH, "//input[@value='CONTINUE']").click()

        wait.until(element_to_be_clickable((By.XPATH, "//a[@class='btn_action cart_button']"))).click()

        time.sleep(2)

        print("Order placed successfully")



try:
    sauce = SauceLabs()
    sauce.cart()
finally:
    driver.quit()