from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, elementname) -> WebElement:
        return WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(elementname)
        )

    def get_elements(self, elementname):
        return WebDriverWait(self.driver, 120).until(
            EC.presence_of_all_elements_located(elementname)
        )

    def wait_for_page_ready(self):
        return WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.execute_script("return document.readyState == 'complete'") is True
        )

    def is_element_visible(self, element_name):
        matching_elements = self.driver.find_elements(*element_name)
        if len(matching_elements) > 0:
            return matching_elements[0].is_displayed()
        else:
            return False
