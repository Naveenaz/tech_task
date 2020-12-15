import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.FormLocators import FormLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import time

class InputFormsCheck(unittest.TestCase):

    #Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome()
        pageUrl = "http://localhost:3000/"
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        self.assertEqual("Welcome to Customer App",
                         self.driver.find_element(By.XPATH, FormLocators.welcome_to_customer_app).text)

    def test_click_submit_without_value(self):
        self.driver.find_element(By.XPATH, FormLocators.submit_button).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

            alert = self.driver.switch_to_alert()
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
        self.assertFalse(self.check_exists_by_xpath(FormLocators.no_of_employees_column))

    def test_table_visible(self):
        self.driver.find_element(By.ID, FormLocators.name_field).send_keys("Test123")
        self.driver.find_element(By.XPATH, FormLocators.submit_button).click()
        time.sleep(5)
        self.assertEqual("Name", self.driver.find_element(By.XPATH, FormLocators.name_column).text)
        self.assertTrue(self.driver.find_element(By.XPATH, FormLocators.no_of_employees_column))
        self.assertTrue(self.driver.find_element(By.XPATH, FormLocators.size_column))

    def test_click_table_single_row(self):
        self.driver.find_element(By.ID, FormLocators.name_field).send_keys("Test123")
        self.driver.find_element(By.XPATH, FormLocators.submit_button).click()
        self.assertEqual("Name", self.driver.find_element(By.XPATH, FormLocators.name_column).text)
        self.assertTrue(self.driver.find_element(By.XPATH, FormLocators.no_of_employees_column))
        self.assertTrue(self.driver.find_element(By.XPATH, FormLocators.size_column))

        self.driver.find_element_by_link_text('Americas Inc.').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element(By.XPATH, "//B[text()='Customer Details']"))

    def test_click_table_multiple_rows(self):
        self.driver.find_element(By.ID, FormLocators.name_field).send_keys("Test123")
        self.driver.find_element(By.XPATH, FormLocators.submit_button).click()
        self.assertEqual("Name", self.driver.find_element(By.XPATH, FormLocators.name_column).text)
        self.assertTrue(self.driver.find_element(By.XPATH, FormLocators.no_of_employees_column))
        self.assertTrue(self.driver.find_element(By.XPATH, FormLocators.size_column))

        self.driver.find_element_by_link_text('Americas Inc.').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element(By.XPATH, "//B[text()='Customer Details']"))

        self.driver.find_element(By.XPATH, "//INPUT[@type='button']").click()
        time.sleep(1)
        self.driver.find_element_by_link_text('United Brands').click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//B[text()='Customer Details']"))

    def check_exists_by_xpath(self, ui_element):
        try:
            self.driver.find_element(By.XPATH, ui_element)
        except NoSuchElementException:
            return False
        return True

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()