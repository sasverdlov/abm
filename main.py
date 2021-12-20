import unittest

import pages
from data import HEADLESS, MAIN_URL, CANONICAL_ATTRIBUTES, ALTERNATE_PROPERTIES
from locators import MainPageLocators
from methods import run_chrome, get_all_element_attributes, compare_lists


class MainPageBaseCases(unittest.TestCase):
    """Class for basic E2E tests for autobidmaster.com"""

    @classmethod
    def setUpClass(cls):
        cls.driver = run_chrome(HEADLESS)

    def setUp(self):
        self.driver.get(MAIN_URL)
        self.main_page = pages.MainPage(self.driver)

    def test_click_abm_logo(self):
        """Tests the ability to click ABM logo to go to main page"""
        url_before = self.driver.current_url
        self.main_page.header.abm_logo.click()
        assert self.driver.current_url == url_before, \
            f'Expected to have URL {url_before}, but after clicking logo it was: {self.driver.current_url}'

    def test_main_page_canonical_alternate(self):
        """Tests canonical and alternate parameters:
        https://yandex.ru/support/webmaster/robot-workings/canonical.html"""
        canonical = self.main_page.driver.find_element(*MainPageLocators.CANONICAL)
        alternate = self.main_page.driver.find_elements(*MainPageLocators.ALTERNATE)

        canonical_attributes = get_all_element_attributes(self.driver, canonical).items()
        assert canonical_attributes == CANONICAL_ATTRIBUTES.items(), f'Expected canonical to have attributes: ' \
                                                                     f'{CANONICAL_ATTRIBUTES.items()}, but got ' \
                                                                     f'{canonical_attributes}'

        alternate_properties = [{'hreflang': x.get_attribute("hreflang"), 'href': x.get_attribute("href")}
                                for x in alternate]
        compare_lists(ALTERNATE_PROPERTIES, alternate_properties, place='alternate properties')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
