from selenium.webdriver.common.by import By


class BasePageLocators:
    # Ссылка "Яндекс" в хедере
    header_yandex_link = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    # Ссылка "Самокат" в хедере
    header_scooter_link = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    # Кнопка "Заказать" в хедере
    header_order_button = (By.XPATH, ".//button[@class='Button_Button__ra12g']")