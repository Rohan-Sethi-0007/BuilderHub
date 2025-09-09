import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class BuilderHubLogin:
    def login(self):
        driver.get("https://buildershubtech.com")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        # Click Login
        driver.find_element(By.XPATH, "//*[@id='basic-navbar-nav']/div/div/a[1]/button").click()

        # Click Register link
        driver.find_element(By.XPATH, "//*[@id='root']/section/div/div[2]/div/form/div[4]/a").click()

        # Enter Company
        company_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter company']")
        company_input.send_keys("hitman")

        # Enter License
        license_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter license number (letters and numbers only)']")
        license_input.send_keys("ABCD1234567890EFGH")

        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='companydetails']/div/div[4]/div/select")))
        dropdown.click()

        # Click one of the options directly by XPath (example: "Home remodeler")
        option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='companydetails']/div/div[4]/div/select/option[@value='2']")))
        option.click()
        print("✅ Selected Home remodeler")
        # Enter Address with Suggestions
        address = driver.find_element(By.XPATH, "//input[@placeholder='Enter address']")
        address.send_keys("Dallas")
        time.sleep(1)  # wait for suggestions

        down_presses = random.randint(1, 3)
        for _ in range(down_presses):
            address.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
        address.send_keys(Keys.ENTER)
        print(f"Selected suggestion number {down_presses}")

        # City
        city = driver.find_element(By.XPATH, "//input[@placeholder='Enter city']")
        city_value = city.get_attribute("value")
        if city_value.strip():
            print("City already contains:", city_value)
        else:
            city.send_keys("Dallas")

        # State
        state = driver.find_element(By.XPATH, "//input[@placeholder='Enter state']")
        state_value = state.get_attribute("value")
        if state_value.strip():
            print("State already contains:", state_value)
        else:
            state.send_keys("Dallas")

        # Wait until pincode field is clickable (ready for typing)
        pincode = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter zip']")))

        # Clear and re-enter to avoid overwrites
        pincode.clear()
        pincode.send_keys("12345")
        time.sleep(0.5)  # tiny wait so JS doesn’t wipe it immediately
        print("✅ Pincode entered:", pincode.get_attribute("value"))

        # Phone Number
        number = driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
        number.send_keys("5875302287")

        # Scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Email
        email = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
        email.send_keys("selina@yopmail.com")

        # Password
        password = driver.find_element(By.XPATH, "//input[@placeholder='Enter password']")
        password.send_keys("Test@123")

        # Confirm Password
        rePass = driver.find_element(By.XPATH, "//input[@autocomplete='new-password']")
        rePass.send_keys("Test@123")

        # Accept Terms
        checkbox = driver.find_element(By.ID, "input-checkbox")
        checkbox.click()

        # Submit
        submit = driver.find_element(By.XPATH, "//*[@id='root']/section/div/div[2]/div/form/button")
        submit.click()
        wait = WebDriverWait(driver, 90)  # 40 seconds timeout
        otp_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='root']/section/div/div[2]/div/form/div[1]/div/div/div[1]/input")  # adjust locator if different
        ))
        print("✅ OTP screen loaded. Please enter OTP manually and click Verify.")

        # Pause script here until you press Enter in terminal
        # input("👉 After entering OTP and clicking Verify, press Enter here to continue...")

        # Wait for the Continue button
        continue_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Complete')]"))
        )

        # Try normal click, fallback to JS click
        try:
            continue_btn.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", continue_btn)

        print("✅ Continue button clicked")

        # Now wait for cardNumber field
        cardNum = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "cardNumber"))
        )
        cardNum.send_keys("4242424242424242")

        expiry = driver.find_element(By.ID, "cardExpiry")
        expiry.click()
        expiry.send_keys("1235")

        cvv = driver.find_element(By.ID, "cardCvc")
        cvv.click()
        cvv.send_keys("123")

        nameCard = driver.find_element(By.ID, "billingName")
        nameCard.click()
        nameCard.send_keys("Testing")

        postalCode = driver.find_element(By.ID, "billingPostalCode")
        postalCode.click()
        postalCode.send_keys("12345")

        print("We have reached till subscribe")
        # Switch back from card iframes to main content
        driver.switch_to.default_content()

        # Wait for Subscribe button to be clickable
        subscribe_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='hosted-payment-submit-button']"))
        )

        # Click using JS (in case normal click fails due to overlay)
        driver.execute_script("arguments[0].click();", subscribe_button)

        print("Welcome to BuilderHubLogin, now lets create some projects")
        print("⏳ Waiting 2 minute after Subscribe...")
        time.sleep(120)
        print("➡️ Moving ahead after wait")


# Run the script
try:
    signUp = BuilderHubLogin()
    signUp.login()
finally:
    driver.quit()
