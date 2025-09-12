import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options to disable password manager popup
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "autofill.profile_enabled": False,
    "autofill.credit_card_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
})
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--incognito")

# Initialize Chrome
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

wait = WebDriverWait(driver, 30)

class employeeCreate:
    def create(self):
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
        #Click on teams link
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/teams']"))).click()

        #Click on add employee button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Employee')]"))).click()

        time.sleep(5)
        #Entering member name
        memberName = driver.find_element(By.XPATH, "//input[@placeholder='Enter member name']")
        memberName.click()
        memberName.send_keys("Gillu don")

        #Enter title
        title = driver.find_element(By.XPATH, "//input[@placeholder='Enter title']")
        title.click()
        title.send_keys("Developer")

        #Enter email
        email = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
        email.click()
        email.send_keys("dondon@yopmail.com")


        #Phone Number
        number = driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
        number.click()
        number.send_keys("5875302290")


        #Enter address
        address = driver.find_element(By.XPATH, "//input[@placeholder='Enter address']")
        address.click()
        address.send_keys("v")

        time.sleep(2)

        address.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        address.send_keys(Keys.ENTER)


        #Press Send Invitation & Continue
        invite = driver.find_element(By.XPATH, "//button[contains(text(),'Send Invitation & Continue')]")
        invite.click()
        print("Employee created successfully")
        time.sleep(5)

try:
    employee = employeeCreate()
    employee.create()
finally:
    driver.quit()

