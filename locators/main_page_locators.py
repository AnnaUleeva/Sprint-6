from selenium.webdriver.common.by import By

from constants import Constants

def create_faq_list():
    faq_list = []
    for i, text in enumerate(Constants.FAQ_PANELS_TEXT, start=0):
        faq_item = {
            'heading': (By.XPATH, f".//div[@class='Home_FAQ__3uVm4']//div[@class='accordion__item'][{i+1}]//div[@class='accordion__heading']"),
            'panel': (By.XPATH, f".//div[@class='Home_FAQ__3uVm4']//div[@class='accordion__item'][{i+1}]//div[@class='accordion__panel']"),
            'text': text
        }
        faq_list.append(faq_item)
    return faq_list

class MainPageLocators:
    # Список локаторов для раздела FAQ
    FAQ_LIST = create_faq_list()
    # Кнопка "Заказать" в разделе FAQ
    ORDER_BUTTON = (By.XPATH, ".//div[@class='Home_RoadMap__2tal_']//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
