import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)
class table():
    def extract_data(self):
        driver.get("https://demoqa.com/webtables")
        driver.maximize_window()

        add_data = driver.find_element(By.ID, "addNewRecordButton")
        add_data.click()

        firstName = driver.find_element(By.ID, "firstName")
        firstName.click()
        firstName.send_keys("Test")

        lastName = driver.find_element(By.ID, "lastName")
        lastName.click()
        lastName.send_keys("User")

        email = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']")
        email.click()
        email.send_keys("testuser@yopmail.com")

        age = driver.find_element(By.ID, "age")
        age.click()
        age.send_keys("24")

        salary = driver.find_element(By.ID, "salary")
        salary.click()
        salary.send_keys("12345")

        department = driver.find_element(By.ID, "department")
        department.click()
        department.send_keys("Testing")

        driver.find_element(By.ID, "submit").click()


        rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
        length = len(rows)
        print(length)
        cols = driver.find_elements(By.CLASS_NAME, "rt-td")
        col_len = len(cols)
        print(col_len)
        table_data = []
        for row in rows:
            row_data = []
            columns = row.find_elements(By.CLASS_NAME, "rt-td")
            for column in columns:
                # columns = driver.find_elements(By.CLASS_NAME, "rt-td")
                # print(i.text)
                cell_text = column.text.strip()
                if cell_text:
                    row_data.append(cell_text)
            if row_data:  # only append non-empty rows
                table_data.append(row_data)  # to store value that have actual data in cells
                print(row_data)

        edit = driver.find_element(By.ID, "edit-record-2")
        edit.click()

        editSalary = driver.find_element(By.ID, "salary")
        time.sleep(2)
        action.double_click(editSalary).perform()
        editSalary.send_keys("10000")

        editSubmit = driver.find_element(By.XPATH, "//button[@type='submit']")
        editSubmit.click()

        driver.find_element(By.ID, "delete-record-2").click()

        search = driver.find_element(By.ID, "searchBox")
        search.click()
        search.send_keys("Vega")
        time.sleep(2)
try:
    data = table()
    data.extract_data()
finally:
    driver.quit()
