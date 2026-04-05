from .base_page import BasePage
from .locators import MainPageLocators
from .test_data import MainPageData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    
    def is_price_range_selection_working(self):
        
        # Используем полную проверку страниц
        # При большом количестве страниц выбираем несколько случайных для ускорения проверки
        max_price_field = self.browser.find_element(*MainPageLocators.MAX_PRICE)
        min_price_field = self.browser.find_element(*MainPageLocators.MIN_PRICE)
        max_price_field.send_keys(MainPageData.MAX_PRICE)
        min_price_field.send_keys(MainPageData.MIN_PRICE)
        
        clean_card_price = self.colecting_price()
        
        assert all(MainPageData.MIN_PRICE <= x <= MainPageData.MAX_PRICE for x in clean_card_price), "Range selection not working. Price out of selected range"
    
    def is_price_sort_working(self):
        
        # Используем полную проверку страниц
        # При большом количестве страниц выбираем несколько случайных для ускорения проверки
        
        select_order = Select(self.browser.find_element(*MainPageLocators.ORDER_OF_SORT))
        select_sort = Select(self.browser.find_element(*MainPageLocators.TYPE_OF_SORT))
        select_sort.select_by_value("price")
        self.is_sort_order_by_asc(select_order)
        self.is_sort_order_by_desc(select_order)
        
        
    def is_sort_order_by_desc(self, order):
        order.select_by_value("desc")
        
        clean_card_price = self.colecting_price()
        
        assert clean_card_price == sorted(clean_card_price, reverse=True),"In sort by price ordering by desc doesn't work"
    
    def is_sort_order_by_asc(self,order):
        order.select_by_value("asc")
        
        clean_card_price = self.colecting_price()
        
        assert clean_card_price == sorted(clean_card_price),"In sort by price ordering by asc doesn't work"
        
    def colecting_price(self):
        
        assert self.is_element_present(*MainPageLocators.PAGE_CONTROLS), "Empty page. No one card on page"
        
        card_price = []
        pages = int(self.browser.find_element(*MainPageLocators.LAST_PAGE).text)
        for p in range(pages):
            card_cur_page_price = self.browser.find_elements(*MainPageLocators.PRICE)
            card_price += [el.text for el in card_cur_page_price]
            
            if p < pages - 1:
                current_first_card = self.browser.find_element(*MainPageLocators.CARD)
                next_page = self.browser.find_element(*MainPageLocators.CHANGE_PAGE)
                next_page.click()
                WebDriverWait(self.browser, 20).until(EC.staleness_of(current_first_card))
        
        fin_price = [int(item.replace('\xa0', '').replace(' ', '').replace('₽', '')) for item in card_price]
        card_price = []
        
        return fin_price
        
    def is_sort_by_category_works(self):
        
        # Используем полную проверку категорий, так как время на их проверку небольшое
        # При большом количестве категорий выбираем важные или несколько случайных
        
        select_cat = self.browser.find_element(*MainPageLocators.CATHEGORY_SELECTOR)
        count = len(Select(select_cat).options)
        for i in range(count):
            select_cat = self.browser.find_element(*MainPageLocators.CATHEGORY_SELECTOR)
            select = Select(select_cat)
            current_option = select.options[i]
        
            if not current_option.get_attribute("value"):
                continue

            old_card = self.browser.find_element(*MainPageLocators.CARD)
            select.select_by_index(i)
            cat_text = current_option.text
            
            WebDriverWait(self.browser, 10).until(EC.staleness_of(old_card))
            pages = int(self.browser.find_element(*MainPageLocators.LAST_PAGE).text)
            for p in range(pages):
                card_categories = self.browser.find_elements(*MainPageLocators.CARD_CATHEGORY)
                card_categories_text = [el.text for el in card_categories]
                
                assert all(text == cat_text for text in card_categories_text), "Sort have card with not selected category"
                if p < pages - 1:
                    
                    current_first_card = self.browser.find_element(*MainPageLocators.CARD)
                    next_page = self.browser.find_element(*MainPageLocators.CHANGE_PAGE)
                    next_page.click()
                    WebDriverWait(self.browser, 10).until(EC.staleness_of(current_first_card))
    
    def is_only_urgent_works(self):
        urgent_btn = self.browser.find_element(*MainPageLocators.PRIOR_CHECKBOX)
        urgent_btn.click()
        
        pages = int(self.browser.find_element(*MainPageLocators.LAST_PAGE).text)
        for i in range(pages):
            assert self.is_elements_count_eq(MainPageLocators.CARD_PRIOR, MainPageLocators.CARD),f" Sort by urgent not working, urgent cards on page: {len(self.browser.find_elements(*MainPageLocators.CARD_PRIOR))}, card on page {len(self.browser.find_elements(*MainPageLocators.CARD))}"
            if i < pages - 1:
                next_page = self.browser.find_element(*MainPageLocators.CHANGE_PAGE)
                next_page.click()
        
    def is_theme_button_work(self):
        cur_theme = self.browser.find_element(*MainPageLocators.THEME_STATUS)
        theme_button = self.browser.find_element(*MainPageLocators.THEME_BTN)
        theme_button.click()
        if cur_theme.text == 'light':
            assert self.is_element_present(*MainPageLocators.DARK_THEME), "Theme doesn't changes"
        elif cur_theme.text == 'dark':
            assert self.is_element_present(*MainPageLocators.LIGHT_THEME), "Theme doesn't changes"
            
    def go_to_stat_page(self):
        stat_page_link = self.browser.find_element(*MainPageLocators.STAT_PAGE_LINK)
        stat_page_link.click()