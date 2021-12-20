from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """Main page locators"""
    HEADER = (By.CLASS_NAME, "page-header")
    ABM_LOGO = (By.CLASS_NAME, "jss230")
    SEARCH_INPUT = (By.CLASS_NAME, "jss235")
    SEARCH_BUTTON = (By.CLASS_NAME, "jss236")
    COPART_LOGO = (By.CLASS_NAME, "jss233")
    LOGIN_BUTTON = (By.CLASS_NAME, "jss248")
    REGISTER_BUTTON = (By.CLASS_NAME, "jss29")

    CANONICAL = (By.XPATH, "//link[@rel='canonical']")
    ALTERNATE = (By.XPATH, "//link[@rel='alternate']")