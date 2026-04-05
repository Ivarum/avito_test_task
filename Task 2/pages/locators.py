from selenium.webdriver.common.by import By

class MainPageLocators():
    STAT_PAGE_LINK = (By.CSS_SELECTOR,"li:last-child a")
    
    CARD = (By.CSS_SELECTOR,"[class*='_card__content']")
    CARD_PRIOR =(By.CSS_SELECTOR,"[class*='_card__priority']")
    PRIOR_CHECKBOX =(By.CSS_SELECTOR,"[class*='_urgentToggle__slider']")
    
    CARD_CATHEGORY =(By.CSS_SELECTOR,"[class*='_card__category']")
    CATHEGORY_SELECTOR =(By.CSS_SELECTOR,"div[class*='_sidebar__content_'] div:nth-child(2) select")
    
    PRICE =(By.CSS_SELECTOR," [class*='_card__price']")
    
    LAST_PAGE = (By.CSS_SELECTOR,"[class*='_pagination__pages'] button:last-child")
    CHANGE_PAGE = (By.CSS_SELECTOR,"div[class*='_pagination__controls'] > button:nth-child(4)")
    PAGE_CONTROLS = (By.CSS_SELECTOR,"[class*='_pagination__controls']")
    
    TYPE_OF_SORT = (By.CSS_SELECTOR,"div[class*='_filtersBar__sort'] div:first-child select")
    ORDER_OF_SORT = (By.CSS_SELECTOR,"div[class*='_filtersBar__sort'] div:last-child select")
    
    MIN_PRICE = (By.CSS_SELECTOR,"div[class*='_filters__priceRange'] input:first-child")
    MAX_PRICE = (By.CSS_SELECTOR,"div[class*='_filters__priceRange'] input:last-child")
    
    THEME_BTN = (By.CSS_SELECTOR,"[class*='_themeToggle']")
    THEME_STATUS = (By.CSS_SELECTOR,"[class*='_themeToggle']")
    LIGHT_THEME = (By.CSS_SELECTOR,"[data-theme]")
    DARK_THEME = (By.CSS_SELECTOR,"[data-theme='dark']")
    
class StatPageLocators():
    REFRESH_BTN =(By.CSS_SELECTOR,"[class*='_refreshButton']")
    
    STOP_BTN =(By.CSS_SELECTOR,"[class*='_timer_'] button[class*='_toggleButton_active']")
    START_BTN =(By.CSS_SELECTOR,"[class*='_timer_'] button[class*='_toggleButton']")
    
    TIMER =(By.CSS_SELECTOR,"[class*='_timeValue']")
    DISABLED_MES =(By.CSS_SELECTOR,"[class*='_disabled']")