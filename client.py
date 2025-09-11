import random
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

class clientMake:
    def create(self):
        driver.get("https://buildershubtech.com")
        driver.maximize_window()

        #login
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='basic-navbar-nav']/div/div/a[1]/button"))).click()

        #Email
        email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter email address']")))
        email.click()
        email.send_keys("selina@yopmail.com")

        #Password
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter password']")))
        password.click()
        password.send_keys("Test@123")

        #Signin
        Actions = ActionChains(driver)
        Actions.send_keys(Keys.ENTER).perform()

        time.sleep(4)
        #If one element is overlapped by another (overlay / loader div to disappear)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[style*='z-index: 9999']")))


        # CRM
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/crm']"))).click()

        #Click on clients
        wait.until(EC.element_to_be_clickable((By.ID, "controlled-tab-example-tab-active"))).click()

        #Click on add client button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Client')]"))).click()

        #Enter name
        name = driver.find_element(By.XPATH, "//input[@placeholder='Enter client name']")
        name.click()
        name.send_keys("Kiteman")

        #Enter Email
        email = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
        email.click()
        email.send_keys("kiteman@yopmail.com")

        #Enter phone number
        phone = driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
        phone.click()
        phone.send_keys("5875302288")

        #Location
        address = driver.find_element(By.XPATH, "//input[@placeholder='Enter street address']")
        address.click()
        address.send_keys("man")
        time.sleep(1)


        #Selecting location from dropdown
        down_press = random.randint(1, 4)
        for _ in range(down_press):
            address.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        address.send_keys(Keys.ENTER)


        #Checking if city is filled or not
        city = driver.find_element(By.XPATH, "//input[@placeholder='Enter city']")
        city_value = city.get_attribute("value")
        if city_value.strip():
            print("City value found")
        else:
            city.send_keys("New York")

        #Checking if state is filled or not
        state = driver.find_element(By.XPATH, "//input[@placeholder='Enter state']")
        state_value = state.get_attribute("value")
        if state_value.strip():
            print("State value was already there")
        else:
            state.send_keys("New York")

        #Checking if ZIP code is found or not
        zipcode = driver.find_element(By.XPATH, "//input[@placeholder='Enter zip']")
        zipcode_value = zipcode.get_attribute("value")
        if zipcode_value.strip():
            print("Zipcode is already filled")
        else:
            zipcode.send_keys("12345")

        #Checkbox
        invite = driver.find_element(By.ID, "checkbox")
        invite.click()
        time.sleep(2)

        # Ensure modal is visible
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

        # Locate Add button inside modal footer
        add = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='modal-footer']//button[normalize-space()='Add']")
            )
        )

        # Scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", add)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", add)

        print("Client added successfully")

        time.sleep(10)
        # #Click on add button
        # # Ensure modal is fully loaded
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        #
        #
        # # Scroll the ADD button into view (important for footer buttons)
        # add = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='ADD']")))
        #
        # driver.execute_script("arguments[0].scrollIntoView(true);", add)
        #
        # # Give a short pause for safety
        # time.sleep(1)
        #
        # # Now click using JS to bypass any overlays
        # driver.execute_script("arguments[0].click();", add)
        #
        # print("Client added successfully")

try:
    clientCreate = clientMake()
    clientCreate.create()
finally:
    driver.quit()


