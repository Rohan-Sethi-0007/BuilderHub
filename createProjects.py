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

wait = WebDriverWait(driver, 15)

class createprojects():
    def create(self):
        driver.get("https://buildershubtech.com/")
        driver.maximize_window()

        # Click Login
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='basic-navbar-nav']/div/div/a[1]/button"))).click()

        # Enter Email
        email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter email address']")))
        email.click()
        email.send_keys("selina@yopmail.com")

        # Enter Password
        password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter password']")))
        password.click()
        password.send_keys("Test@123")

        # Press ENTER
        Actions = ActionChains(driver)
        Actions.send_keys(Keys.ENTER).perform()

        //hi there how are you lauds lehsan

        # Wait for Add button
        add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/section[1]/div/div[1]/div[2]/div/button")))
        add.click()

        # Select client
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), ' Find Existing')]"))).click()

        # Skip client
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-outline-secondary'][2]"))).click()

        # Select project type
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/h4"))).click()

        # Click on next button
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/button[2]"))).click()

        # Enter project title
        projectName = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter project title']")))
        projectName.click()
        projectName.send_keys("Remodelling")

        # Select start date
        startDate = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select start date']")))
        startDate.click()

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__day react-datepicker__day--018"))).click()

        # Click next buttons
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-primary"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-outline-secondary"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-outline-secondary"))).click()

        # Select project image
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "projecttypeimg"))).click()

        # Finish
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Finish')]"))).click()


try:
    projects = createprojects()
    projects.create()
finally:
    driver.quit()
