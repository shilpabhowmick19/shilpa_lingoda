from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This page contains all generic methods"""


class TestDataMVC:
    welcome_text = "Helping you select an MV* framework"
    base_url = "https://todomvc.com/"
    page_title = "TodoMVC"
    tab_js_name = "JavaScript"
    polymer_url = "https://todomvc.com/examples/polymer/index.html"
    firstitem = "TEST001"
    seconditem = "TEST002"
    appendtext = "@@"
    newseconditem = "TEST002@@"


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

