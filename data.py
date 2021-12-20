HEADLESS = False
ADBLOCK_CRX_PATH = 'external_files/adblock_4_39_1_0.crx'
MAIN_URL = 'https://www.autobidmaster.com/'

CANONICAL_ATTRIBUTES = {'href': f'{MAIN_URL}ru/', 'rel': 'canonical'}
ALTERNATE_PROPERTIES = \
    [{'hreflang': 'en', 'href': 'https://www.autobidmaster.com/en/'},
     {'hreflang': 'ru-UA', 'href': 'https://www.autobidmaster.com/ru/'},
     {'hreflang': 'ru-RU', 'href': 'https://www.autobidmaster.com/ru/'},
     {'hreflang': 'ru-GE', 'href': 'https://www.autobidmaster.com/ru/'},
     {'hreflang': 'ru-BY', 'href': 'https://www.autobidmaster.com/ru/'},
     {'hreflang': 'es', 'href': 'https://www.autobidmaster.com/es/'},
     {'hreflang': 'pl', 'href': 'https://www.autobidmaster.com/pl/'},
     {'hreflang': 'ka', 'href': 'https://www.autobidmaster.com/ka/'},
     {'hreflang': 'ar', 'href': 'https://www.autobidmaster.com/ar/'},
     {'hreflang': 'de', 'href': 'https://www.autobidmaster.com/de/'},
     {'hreflang': 'bg', 'href': 'https://www.autobidmaster.com/bg/'},
     {'hreflang': 'ro', 'href': 'https://www.autobidmaster.com/ro/'},
     {'hreflang': 'x-default', 'href': 'https://www.autobidmaster.com/en/'}]
# language = driver.execute_script("return window.navigator.userLanguage || window.navigator.language")