from test_base import TestBase
from selenium.webdriver.common.by import By
import time


class DemoTest(TestBase):

    def test_demo(self):
        self.driver.get('https://www.google.com/')
        self.driver.find_element(By.ID, 'lst-ib').send_keys('python')
        return time.sleep(1)