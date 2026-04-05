import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default='en',
                     help="Choose your language: ru, en, ec, fr",)
    parser.addoption('--on_mobile', action='store', default='off',
                     help="Choose on mobile off or on (only for Chrome)",)

@pytest.fixture(scope="function")
def browser(request):
    
    mobile = request.config.getoption("--on_mobile")
    mobile_emulation = { "deviceName": "Samsung Galaxy S20 Ultra" }
    
    user_language = request.config.getoption("--language")
    options = Options()
    if mobile == "on":
        options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    options.add_argument(f"--lang={user_language}")

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser_name = request.config.getoption("browser_name")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()
    

