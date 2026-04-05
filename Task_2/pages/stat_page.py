from .base_page import BasePage
import pytest
from .locators import StatPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StatPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(StatPage, self).__init__(*args, **kwargs)
    
    def is_update_func_working(self):
        self.is_update_btn_working()
        self.is_stop_update_btn_working()
        self.is_start_update_btn_working()
        
    def is_update_btn_working(self):
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(StatPageLocators.TIMER, "4:56")
            )
        before_timer = self.browser.find_element(*StatPageLocators.TIMER).text
        
        update_btn = self.browser.find_element(*StatPageLocators.REFRESH_BTN)
        update_btn.click()
        after_timer = self.browser.find_element(*StatPageLocators.TIMER).text
        assert time_to_seconds(before_timer) < time_to_seconds(after_timer) , "Timer doesn't update. Refresh button don't working "
        
    def is_stop_update_btn_working(self):
        update_stop_btn = self.browser.find_element(*StatPageLocators.STOP_BTN)
        update_stop_btn.click()
        
        results = {
        "Timer is still present": self.is_not_element_present(*StatPageLocators.TIMER),
        "Message about disable is missing": self.is_element_present(*StatPageLocators.DISABLED_MES),
        "Start timer button is missing": self.is_element_present(*StatPageLocators.START_BTN)
        }
        
        assert all(results.values()), f"UI state mismatch: {[msg for msg, res in results.items() if not res]}"
        
    def is_start_update_btn_working(self):
        
        update_start_btn = self.browser.find_element(*StatPageLocators.START_BTN)
        update_start_btn.click()
        
        results = {
        "Timer doesn't present": self.is_element_present(*StatPageLocators.TIMER),
        "Message about disable is still present": self.is_not_element_present(*StatPageLocators.DISABLED_MES),
        "Start timer button is still present": self.is_not_element_present(*StatPageLocators.START_BTN)
        }

        assert all(results.values()), f"UI state mismatch: {[msg for msg, res in results.items() if not res]}"

    
def time_to_seconds(t_str):
    minutes, seconds = map(int, t_str.strip().split(':'))
    return minutes * 60 + seconds