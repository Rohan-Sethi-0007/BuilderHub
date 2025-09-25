import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)
class dropdown():
    def downdrop(self):
        driver.get("https://demoqa.com/select-menu")
        driver.maximize_window()

        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='withOptGroup']"))
        )

        option.click()
        input = wait.until(EC.visibility_of_element_located((By.ID, "react-select-2-input")))
        input.send_keys("group 2")

        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ENTER).perform()
        time.sleep(2)

        single = driver.find_element(By.XPATH, "//div[@id='selectOne']//div[@class=' css-yk16xz-control']")
        single.click()
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ENTER).perform()

        time.sleep(2)

        dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))

        # Select by visible text
        dropdown.select_by_visible_text("Green")
        time.sleep(2)
        # Select by value
        dropdown.select_by_value("6")
        time.sleep(2)
        # Select by index (0-based)
        dropdown.select_by_index(4)
        time.sleep(2)

        dropdowns = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-2b097c-container")))
        multiselect = wait.until(EC.element_to_be_clickable(dropdowns[2]))
        driver.execute_script("arguments[0].scrollIntoView(true);", multiselect)
        multiselect.click()

        input = driver.find_element(By.ID,"react-select-4-input")
        input.send_keys("green")
        input.send_keys(Keys.ENTER)
        input.send_keys("black")
        input.send_keys(Keys.ENTER)
        action.send_keys(Keys.ESCAPE).perform()

        time.sleep(2)

        standard = Select(driver.find_element(By.ID, "cars"))
        standard.select_by_visible_text("Volvo")
        standard.select_by_value("opel")

        time.sleep(2) 

try:
    selection = dropdown()
    selection.downdrop()
finally:
    driver.quit()