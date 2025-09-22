import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
)

wait = WebDriverWait(driver, 20)
class hoverTry():
    def hoverOver(self):
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        driver.find_element(By.XPATH, "//a[@href='/hovers']").click()

        time.sleep(3)

        # image = driver.find_element(By.XPATH, "//div[@class='example']//div[@class='figure'][1]//img")
        action = ActionChains(driver)
        # action.move_to_element(image).perform()
        #
        # text_element = wait.until(visibility_of_element_located((By.XPATH, "//div[@class='example']//div[@class='figcaption']/h5")))
        # print(text_element.text)

        time.sleep(2)

        for i in range(1, 4):  # loop through 1,2,3
            image = driver.find_element(By.XPATH, f"//div[@class='example']//div[@class='figure'][{i}]//img")
            action.move_to_element(image).perform()

            text_element = wait.until(
                visibility_of_element_located(
                    (By.XPATH, f"//div[@class='example']//div[@class='figure'][{i}]//div[@class='figcaption']/h5"))
            )
            print(text_element.text)
            time.sleep(1)

try:
    over = hoverTry()
    over.hoverOver()
finally:
    driver.quit()
