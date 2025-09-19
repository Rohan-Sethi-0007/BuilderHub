import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
)

wait = WebDriverWait(driver, 20)
class drag():
    def drop(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//a[@href='/drag_and_drop']").click()

        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")

        action = ActionChains(driver)
        # action.click_and_hold(source).move_to_element(target).release().perform()
        action.drag_and_drop(source,target).perform()

        time.sleep(5)
        print("A and B interchanged, please check")

try:
    drag_drop = drag()
    drag_drop.drop()
finally:
    driver.quit()


