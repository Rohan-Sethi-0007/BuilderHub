import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

action = ActionChains(driver)
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
class drag():
    def drop(self):

        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")

        ActionChains(driver).drag_and_drop(source, target).perform()

    def accept(self):

        driver.find_element(By.ID, "droppableExample-tab-accept").click()

        time.sleep(4)
        acceptable = driver.find_element(By.ID, "acceptable")
        not_acceptable = driver.find_element(By.ID, "notAcceptable")
        target = driver.find_element(By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']")

        action.drag_and_drop(not_acceptable, target).perform()
        time.sleep(2)

        print("After Not Acceptable Drop:", target.text)
        print("Target Color:", target.value_of_css_property("background-color"))

        action.drag_and_drop(acceptable, target).perform()

        print("After Acceptable Drop: ",target.text)
        print("Background color has been changed: ",target.value_of_css_property("background-color"))

    def propogation(self):

        driver.find_element(By.ID,"droppableExample-tab-preventPropogation").click()
        source = driver.find_element(By.XPATH, "//div[@id='droppableExample-tabpane-preventPropogation']//div[@id='dragBox']")
        target1 = driver.find_element(By.XPATH, "//div[@class='pp-drop-container']//div[@id='notGreedyDropBox']")
        target2 = driver.find_element(By.XPATH, "//div[@class='pp-drop-container']//div[@id='notGreedyInnerDropBox']")

        action.drag_and_drop(source,target1).perform()

        print("Text changes to:", target1.text)
        print("Background color code of non greedy inner box changes to:", target1.value_of_css_property("background-color"))
        time.sleep(2)
        print("Text changes to:", target2.text)
        print("Background color code should be same as outer:", target2.value_of_css_property("background-color"))

        target3 = driver.find_element(By.XPATH, "//div[@class='pp-drop-container']//div[@id='greedyDropBoxInner']")
        target4 = driver.find_element(By.XPATH, "//div[@class='pp-drop-container']//div[@id='greedyDropBox']")

        # to displayed as drag and drop sometimes directlt drops skipping hover effects
        action.click_and_hold(source).move_to_element(target3).pause(1).release().perform()


        print("Text changes to:", target3.text)
        print("Background color of greedy inner box is: ",target3.value_of_css_property("background-color"))
        time.sleep(2)

        action.click_and_hold(source).move_to_element(target4).pause(3).release().perform()
        print("Text changes to:", target4.text)
        time.sleep(3)
        print("Background color of greedy outer", target4.value_of_css_property("background-color"))
        time.sleep(2)

    def revert(self):
         driver.find_element(By.ID, "droppableExample-tab-revertable").click()

         source1 = driver.find_element(By.XPATH, "//div[@id='revertableDropContainer']//div[@id='revertable']")
         source2 = driver.find_element(By.XPATH, "//div[@id='revertableDropContainer']//div[@id='notRevertable']")
         target = driver.find_element(By.XPATH, "//div[@id='revertableDropContainer']//div[@id='droppable']")

         original_postion = source1.location
         action.click_and_hold(source1).move_to_element(target).pause(2).release().perform()
         new_position = source1.location
         if original_postion == new_position:
            print("It is not reverted")
         else:
            print("It is reverted")

         time.sleep(2)

         original_position2 = source2.location
         action.click_and_hold(source2).move_to_element(target).pause(2).release().perform()
         new_position2 = source2.location
         if original_position2 == new_position2:
            print("It is not reverted")
         else:
            print("status changed: ",target.text)
            print("Background color changes to: ", target.value_of_css_property("background-color"))

try:
    dragging = drag()
    # dragging.drop()
    # dragging.accept()
    # dragging.propogation()
    dragging.revert()
finally:
    driver.quit()

