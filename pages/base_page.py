from datetime import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except:
            return print("element not found!")

    def do_click_in_hurry(self, by_locator):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).click()
        except:
            return print("element not found! scrolling down!")

    def do_send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except:
            return print("element not found!")

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except:
            return print("element not found!")

    def is_element_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except:
            return False

    def is_element_visible_in_hurry(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except:
            return False

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def sleep(self, param):
        sleep(param)

    def find_elements(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(locator))
            self.sleep(1)
            array = self.driver.find_elements_by_css_selector(locator)
            return array
        except:
            return "elements not found"





