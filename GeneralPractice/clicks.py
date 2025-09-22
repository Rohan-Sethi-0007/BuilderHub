import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 20)
action = ActionChains(driver)

class click():
    def doubleClick(self):
        driver.get("https://demoqa.com/buttons")
        driver.maximize_window()

        double = driver.find_element(By.ID, "doubleClickBtn")
        action.double_click(double).perform()
        msg = wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
        print(msg.text)


    def rightClick(self):
        driver.get("https://demoqa.com/buttons")
        driver.maximize_window()

        right = driver.find_element(By.ID, "rightClickBtn")
        action.context_click(right).perform()
        msg = wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage")))
        print(msg.text)

    def randomClick(self):
        driver.get("https://demoqa.com/buttons")
        driver.maximize_window()

        Rclick = driver.find_element(By.XPATH, "//button[text()='Click Me']")
        action.click(Rclick).perform()

        msg = wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage")))
        print(msg.text)

try:
    clickPractice = click()
    clickPractice.doubleClick()
    time.sleep(2)
    clickPractice.rightClick()
    time.sleep(2)
    clickPractice.randomClick()
    time.sleep(2)
finally:
    driver.quit()

