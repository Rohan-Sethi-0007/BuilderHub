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

class contractor():
    def sub(self):
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

        #Click on team
        driver.find_element(By.XPATH, "//a[@href='/teams']").click()

        wait.until(element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Vendors')]"))).click()
        time.sleep(5)


        #Click on add vendor button
        driver.find_element(By.XPATH,"//*[@id='root']/div[2]/section[1]/div/div[1]/div[2]/div/button").click()

        time.sleep(5)
        #Entering vendor name
        name = driver.find_element(By.XPATH, "//input[@placeholder='Enter vendor name']")
        name.click()
        name.send_keys("chota don")

        #vendor type
        type = driver.find_element(By.XPATH, "//div[contains(text(),'Select subcontractor type')]")
        type.click()

        # Wait and select first option
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Active User')]"))).click()

        time.sleep(5)

        #License number
        license = driver.find_element(By.XPATH, "//input[@placeholder='Enter license number']")
        license.click()
        license.send_keys("123456QWERTYU")

        #Phone number
        phone = driver.find_element(By.XPATH,"//input[@placeholder='1 (702) 123-4567']")
        phone.click()
        phone.send_keys("5875302291")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #Input trade
        trade = driver.find_element(By.XPATH, "//input[@placeholder='Enter trade']")
        trade.click()
        trade.send_keys("Design")

        #Enter email
        email = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
        email.click()
        email.send_keys("diggle@yopmail.com")

        #Invite and Apply
        invite = driver.find_element(By.XPATH, "//button[contains(text(), 'Invite and Apply')]")
        invite.click()

        time.sleep(5)

try:
    vendor = contractor()
    vendor.sub()
finally:
    driver.quit()

