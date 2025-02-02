from selenium.webdriver.common.by import By

FAQ_LIST_LEN = 8

def create_faq_list():
    faq_list = []
    for i in range(FAQ_LIST_LEN):
        faq_item = {
            'heading': (By.XPATH, f".//div[@class='Home_FAQ__3uVm4']//div[@class='accordion__item'][{i+1}]//div[@class='accordion__heading']"),
            'panel': (By.XPATH, f".//div[@class='Home_FAQ__3uVm4']//div[@class='accordion__item'][{i+1}]//div[@class='accordion__panel']")
        }
        faq_list.append(faq_item)
    return faq_list

class MainPageLocators:
    # Список локаторов для раздела FAQ
    faq_list = create_faq_list()
    # Кнопка "Заказать" в разделе FAQ
    order_button = (By.XPATH, ".//div[@class='Home_RoadMap__2tal_']//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
