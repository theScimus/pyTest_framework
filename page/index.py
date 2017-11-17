from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.support.wait import WebDriverWait

from utils import ELEMENT_WAIT_TIMEOUT, ROOT_URL
from page.page import Page

class IndexPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get(ROOT_URL)
        return self