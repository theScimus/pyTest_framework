from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.support.wait import WebDriverWait

from page.page import Page
from utils import ELEMENT_WAIT_TIMEOUT

class DashboardPage(Page):

    def __init__(self, driver):
        super().__init__(driver)