from selenium.webdriver.common.by import By


class FormLocators(object):
    welcome_to_customer_app = "//H1[text()='Welcome to Customer App']"
    name_field = "name"
    submit_button = "//INPUT[@type='button']"
    name_column = "//TH[text()='Name']"
    no_of_employees_column = "//TH[text()='# of Employees']"
    size_column = "//TH[text()='Size']"
