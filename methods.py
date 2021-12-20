from unicodedata import normalize

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

from data import ADBLOCK_CRX_PATH


def run_chrome(headless=False, incognito=False, adblock=False):
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'performance': 'ALL'}
    opt = webdriver.ChromeOptions()
    if headless:
        opt.add_argument("--headless")
    if incognito:
        opt.add_argument('--incognito')
    if adblock:
        opt.add_extension(ADBLOCK_CRX_PATH)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=opt, desired_capabilities=d, keep_alive=True)
    browser.set_page_load_timeout(10)
    return browser


def get_all_element_attributes(driver, element):
    attrs = driver.execute_script(
        '''var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) 
        { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;''',
        element)
    return attrs


def check_color_of_element(element, r, g, b, a=1, background=False):
    prop = "background-color" if background else "color"
    return element.value_of_css_property(prop) == f'rgba({r}, {g}, {b}, {a})'


def compare_lists(expected_list, actual_list, place=None, unify_enc=True):
    if unify_enc:
        expected_list, actual_list = [normalize('NFKD', x) if isinstance(x, list) else x for x in expected_list], \
                                     [normalize('NFKD', x) if isinstance(x, list) else x for x in actual_list]
    shortage = [x for x in expected_list if x not in actual_list]
    excess = [x for x in actual_list if x not in expected_list]
    placeholder = f' in {place}' if place else ''
    shortage_error = f'Elements were expected{placeholder}, but not found: {shortage}'
    excess_error = f'Elements were not expected{placeholder}, but found: {excess}'
    assert len(shortage) == 0, shortage_error
    assert len(excess) == 0, excess_error
