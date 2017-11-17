import sys
import os
from selenium import webdriver

ELEMENT_WAIT_TIMEOUT = 15


def get_config():
    from utils.config import Config
    return Config().configuration

REQUESTS_WAIT_TIMEOUT = 15
ROOT_URL = get_config()["environments"]["url"]


def get_driver():
    executable_path = os.path.join('drivers', sys.platform, 'chromedriver')
    if sys.platform == 'win32':
        executable_path += '.exe'
    driver = webdriver.Chrome(executable_path=executable_path)
    return driver


def take_screenshot(driver, name=None):
    platform = driver.capabilities['platform']
    browser = driver.capabilities['browserName']
    browser_version = driver.capabilities['version']
    file_name = 'screenshots/{}/{}/{}/{}.png'.format(
        platform,
        browser.replace(' ', ''),
        browser_version,
        name if name else sys._getframe().f_back.f_code.co_name)  # inspect.stack()[1][3]
    os.makedirs(os.path.split(file_name)[0], exist_ok=True)
    with open(file_name, 'wb') as screenshot_file:
        screenshot_file.write(driver.get_screenshot_as_png())
