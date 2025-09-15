import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options to disable password manager popup
chrome_options = Options()

chrome_options.add_argument("--incognito")

# Initialize Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

wait = WebDriverWait(driver, 30)

class clientAssign():
    def clients(self):
        driver.get("https://buildershubtech.com")
        driver.maximize_window()

        # login
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='basic-navbar-nav']/div/div/a[1]/button"))).click()

        # Email
        email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter email address']")))
        email.click()
        email.send_keys("felicity@yopmail.com")

        # Password
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter password']")))
        password.click()
        password.send_keys("Test@123")

        Actions = ActionChains(driver)
        Actions.send_keys(Keys.ENTER).perform()

        time.sleep(5)

        add = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/section[1]/div/div[1]/div[2]/div/button")))
        add.click()

        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), ' Find Existing')]"))).click()

        time.sleep(3)

        clientClick = wait.until(EC.presence_of_all_elements_located((By.XPATH,
        "//div[@class='clientModal_scroll w-100']//div[@class='w-100 clientlist  card']")))

        clientClick[0].click()

        next = driver.find_element(By.XPATH, "//button[contains(text(), 'Next Step')]")
        next.click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[contains(text(), 'Next Step')]").click()

        time.sleep(3)

        kitchen_remodel = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//h4[normalize-space(text())='Kitchen Remodel']"))
        )
        kitchen_remodel.click()

        # Now click the Next step button
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next Step')]"))
        )
        driver.execute_script("arguments[0].click();", next_button)

        # Now wait for the project title input
        projectName = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter project title']"))
        )
        projectName.click()
        projectName.send_keys("Kitchen Remodel")

        # Select start date
        startDate = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select start date']")))
        startDate.click()

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'react-datepicker__day--024')]"))
        ).click()

        driver.find_element(
            By.XPATH, "//h2[normalize-space()='Projects Schedule']/following::button[contains(text(),'Next Step')]"
        ).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Skip']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Skip For Now']"))).click()

        # Select subcontractor or skip
        subcontract = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[3]/div/div")))
        subcontract.click()


        # Finish
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Finish')]"))).click()
        time.sleep(10)

        print("Project created successfully")

try:
    Automate = clientAssign()
    Automate.clients()
finally:
    driver.quit()

