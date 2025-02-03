from selenium.webdriver.common.by import By


class BasePageLocators:
    # Ссылка "Яндекс" в хедере
    HEADER_YANDEX_LINK = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    # Ссылка "Самокат" в хедере
    HEADER_SCOOTER_LINK = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    # Кнопка "Заказать" в хедере
    HEADER_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")