from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators


class BaseObject(object):
    """Base class for PageObject"""

    def __init__(self, driver, locator=None):
        self.driver = driver
        self.locator = locator

    def make_screenshot(self, file_name):
        """Added waiting of element presence to basic method"""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locator))
        screenshot = element.screenshot_as_png
        with open(file_name, 'wb') as f:
            f.write(screenshot)


class BasePage(BaseObject):
    """Base class to initialize the page"""

    def __init__(self, driver):
        super().__init__(driver)

    def get_element(self, locator, timeout=2.0):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))


class MainPage(BasePage):
    """Main page of autobidmaster.com"""

    def __init__(self, driver):
        super().__init__(driver)
        self.header = self.get_element(MainPageLocators.HEADER)
        self.header.abm_logo = self.get_element(MainPageLocators.ABM_LOGO)
        self.header.copart_logo = self.get_element(MainPageLocators.COPART_LOGO)
        self.header.search_input = self.get_element(MainPageLocators.SEARCH_INPUT)
        self.header.search_button = self.get_element(MainPageLocators.SEARCH_BUTTON)
        self.header.login_button = self.get_element(MainPageLocators.LOGIN_BUTTON)
        self.header.register_button = self.get_element(MainPageLocators.REGISTER_BUTTON)

