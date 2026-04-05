from .pages.stat_page import StatPage
from .pages.main_page import MainPage
import pytest

link = "https://cerulean-praline-8e5aa6.netlify.app"
class TestStatPageFunc():
    def test_is_timer_function_works(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_stat_page()
        stat_page = StatPage(browser, browser.current_url)
        stat_page.is_update_func_working()
