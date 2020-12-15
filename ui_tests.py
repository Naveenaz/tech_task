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

    # def test_invalid_url(self):
    #     self.driver.find_element(By.ID, "url").click()
    #     self.driver.find_element(By.ID, "url").send_keys(FormLocators.invalid_url)
    #     self.assertEqual("Invalid URL format.", self.driver.find_element(By.XPATH, FormLocators.invalid_url_message).text)
    #
    # def test_name_field(self):
    #     self.driver.find_element(By.ID, "fullName").click()
    #     self.driver.find_element(By.ID, "fullName").send_keys("Naveen")
    #     time.sleep(1)
    #     element = self.driver.find_element(By.ID, "fullName")
    #     self.assertEqual("Naveen", element.get_attribute('value'))
    #
    # def test_name_field_after_save(self):
    #     self.driver.find_element(By.ID, "fullName").click()
    #     self.driver.find_element(By.ID, "fullName").send_keys("Naveen")
    #     self.save_button()
    #     self.handle_pop_up()
    #     element = self.driver.find_element(By.ID, "fullName")
    #     self.assertEqual("Naveen", element.get_attribute('value'))
    #
    # def test_country_field(self):
    #     self.driver.find_element(By.ID, "country").click()
    #     self.driver.find_element(By.ID, "country").send_keys("India")
    #     time.sleep(1)
    #     element = self.driver.find_element(By.ID, "country")
    #     self.assertEqual("India", element.get_attribute('value'))
    #
    # def test_country_field_after_save(self):
    #     self.driver.find_element(By.ID, "country").click()
    #     self.driver.find_element(By.ID, "country").send_keys("India")
    #     self.save_button()
    #     self.handle_pop_up()
    #     element = self.driver.find_element(By.ID, "country")
    #     self.assertEqual("India", element.get_attribute('value'))
    #
    # def test_position_field(self):
    #     self.driver.find_element(By.ID, "position").click()
    #     self.driver.find_element(By.ID, "position").send_keys("Test")
    #     time.sleep(1)
    #     element = self.driver.find_element(By.ID, "position")
    #     print(element.get_attribute('value'))
    #     self.assertEqual("Test", element.get_attribute('value'))
    #
    # def test_position_field_after_save(self):
    #     self.driver.find_element(By.ID, "position").click()
    #     self.driver.find_element(By.ID, "position").send_keys("Test")
    #     self.save_button()
    #     self.handle_pop_up()
    #     element = self.driver.find_element(By.ID, "position")
    #     print(element.get_attribute('value'))
    #     self.assertEqual("Test", element.get_attribute('value'))
    #
    # def test_add_test_user_all_fields_and_save(self):
    #     test_user = 'Naveen Interview'
    #     self.driver.find_element(By.ID, "fullName").click()
    #     self.driver.find_element(By.ID, "fullName").send_keys(test_user)
    #     self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) > .position-relative").click()
    #     self.driver.find_element(By.ID, "country").click()
    #     self.driver.find_element(By.ID, "country").click()
    #     self.driver.find_element(By.ID, "country").send_keys("India")
    #     self.driver.find_element(By.CSS_SELECTOR, ".form").click()
    #     self.driver.find_element(By.NAME, "yob").click()
    #     self.driver.find_element(By.NAME, "yob").send_keys("2020-05-08")
    #     self.driver.find_element(By.ID, "position").click()
    #     self.driver.find_element(By.ID, "position").send_keys("Test")
    #     self.driver.find_element(By.ID, "url").click()
    #     self.driver.find_element(By.ID, "url").click()
    #     self.driver.find_element(By.ID, "url").click()
    #     self.driver.find_element(By.ID, "url").send_keys(FormLocators.valid_url)
    #
    #     # Schedule next hour
    #     select = Select(self.driver.find_element(By.ID, "risk"))
    #
    #     select.select_by_visible_text('Low')
    #
    #     self.save_button()
    #     self.assertIn("You added " + test_user,
    #                   self.driver.find_element(By.XPATH, FormLocators.save_popup_message).text)
    #     self.handle_pop_up()
    #
    # def test_incorrect_date(self):
    #     test_user = 'Naveen Interview'
    #     self.driver.find_element(By.ID, "fullName").click()
    #     self.driver.find_element(By.ID, "fullName").send_keys(test_user)
    #     self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) > .position-relative").click()
    #     self.driver.find_element(By.ID, "country").click()
    #     self.driver.find_element(By.ID, "country").click()
    #     self.driver.find_element(By.ID, "country").send_keys("India")
    #     self.driver.find_element(By.CSS_SELECTOR, ".form").click()
    #     self.driver.find_element(By.NAME, "yob").click()
    #     self.driver.find_element(By.NAME, "yob").send_keys("2020-32-32")
    #     time.sleep(5)
    #     # Not sure how to add assert here as date field doesn't give any error or warning

    def save_button(self):
        # Save button
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, FormLocators.save_button).click()
        time.sleep(10)

    def handle_pop_up(self):
        self.driver.find_element(By.XPATH, FormLocators.back_button_pop_up).click()
        time.sleep(5)

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