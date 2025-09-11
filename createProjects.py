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

        # Wait for Add button
        add = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/section[1]/div/div[1]/div[2]/div/button")))
        add.click()

        # Select client
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), ' Find Existing')]"))).click()

        # Skip client
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-outline-secondary'][2]"))).click()

        # Wait for the project type container to load
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/div")))

        # Click Kitchen Remodel
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
        projectName.send_keys("Renovation")

        # Select start date
        startDate = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select start date']")))
        startDate.click()

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'react-datepicker__day--018')]"))
        ).click()

        # Click next buttons
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn btn-primary')]"))).click()
        # next_button2 = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//div[contains(@class,'project-footer')]//button[contains(text(),'Next Step')]")
        #     )
        # )


        #driver.execute_script("arguments[0].click();", next_button2)

        driver.find_element(
            By.XPATH, "//h2[normalize-space()='Projects Schedule']/following::button[contains(text(),'Next Step')]"
        ).click()


        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Skip']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Skip For Now']"))).click()

        # Select project image
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "projecttypeimg"))).click()

        # Finish
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Finish')]"))).click()


try:
    projects = createprojects()
    projects.create()
finally:
    driver.quit()
