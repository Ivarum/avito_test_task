from .pages.main_page import MainPage
import pytest

link = "https://cerulean-praline-8e5aa6.netlify.app"
@pytest.mark.mobile
class TestMainPageMobileFunc():
    
    def test_can_mobile_user_change_theme(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.is_theme_button_work()