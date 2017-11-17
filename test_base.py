import unittest
import time
from utils import get_config
from utils import get_driver

class TestBase(unittest.TestCase):

    def setUp(self):
        self.config = get_config()
        self.driver = get_driver()
        time.sleep(0.5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
