from .pages.main_page import MainPage
import pytest

link = "https://cerulean-praline-8e5aa6.netlify.app"
@pytest.mark.desktop_ver
class TestMainPageFunc():
    
    def test_can_user_apply_price_range_selection(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.is_price_range_selection_working()
    
    def test_can_user_apply_sort_by_price(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.is_price_sort_working()
        
    def test_can_user_apply_sort_by_category(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.is_sort_by_category_works()
        
    def test_can_user_apply_only_urgent_advertisement(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.is_only_urgent_works()
    
        
        