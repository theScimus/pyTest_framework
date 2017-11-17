from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utils import REQUESTS_WAIT_TIMEOUT

import string, random

class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def hover(self, element):
        link = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(element),'There is no element')
        return ActionChains(self.driver).move_to_element(link).perform()

    def click(self, element):
        link = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(element))
        return link.click()

    def validate_elements(self, element, index):
        self.driver.implicitly_wait(2)
        return self.driver.find_elements(*element)[index].text


    def validate_element_attribute_value(self, element):
        self.driver.implicitly_wait(2)
        return self.driver.find_element(*element).get_attribute('value')

    def find_element(self, element):
        self.driver.implicitly_wait(2)
        return self.driver.find_element(*element)

    def find_elements(self, element):
        self.driver.implicitly_wait(2)
        return self.driver.find_elements(*element)

    def validate_element(self, element):
        self.driver.implicitly_wait(2)
        return self.driver.find_element(*element).text

    def element_should_not_exist(self, element):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element(*element)
        except NoSuchElementException:
            return True
        raise TypeError("The element exist on the page, but shouldn't")

    def elements_should_not_exist(self, element, index):
        try:
            self.driver.find_elements(*element)[index]
        except NoSuchElementException:
            return True
        raise TypeError("The element exist on the page, but shouldn't")

    def random_email(self, element):
        randtext = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
        random_email = "test+"+randtext+"@gmail.com"
        self.email = random_email
        return self.driver.find_element(*element).send_keys(random_email)

    def random_name(self, element):
        randtext = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        return self.driver.find_element(*element).send_keys(randtext)

    def random_digits(self, element):
        randtext = ''.join([random.choice(string.digits) for n in range(10)])
        return self.driver.find_element(*element).send_keys(randtext)

    def send_text(self, element, text):
        self.driver.implicitly_wait(5)
        return self.driver.find_element(*element).send_keys(*text)