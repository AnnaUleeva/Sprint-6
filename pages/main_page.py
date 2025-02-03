import time

import allure

from constants import Constants
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Прокуртка до кнопки "Заказать" и нажатие на нее')
    def click_order_button(self):
        self.scroll_to_element_by_locator(MainPageLocators.ORDER_BUTTON)
        self.wait_visible_element(MainPageLocators.ORDER_BUTTON)
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Прокрутка до вопроса FAQ, нажатие на него и проверка открытия текста')
    def open_faq(self, heading_locator, panel_locator):
        self.wait_visible_element(heading_locator)
        self.scroll_to_element_by_locator(heading_locator)
        time.sleep(0.5)
        self.wait_visible_element(heading_locator)
        self.click_element(heading_locator)
        # self.wait_visible_element(heading_locator)
        self.wait_visible_element(panel_locator)
        self.scroll_to_element_by_locator(panel_locator)
        return self.find_element(panel_locator).is_displayed()

    @allure.step('Получение текста элемента')
    def get_faq_text(self, panel_locator):
        return self.get_text(panel_locator)






