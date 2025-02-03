import allure
import pytest
from selenium import webdriver

from constants import Constants
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestFaqOpen:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка открытия элемнтов в блоке FAQ')
    @allure.description('Переходим к блоку, кликаем по заголовку вопроса, проверяем видимость ответа' )
    @pytest.mark.parametrize('list_item', MainPageLocators.FAQ_LIST)
    def test_faq_open(self, list_item):
        self.driver.get(Constants.BASE_URL)
        main_page = MainPage(self.driver)
        is_opened_faq = main_page.open_faq(list_item['heading'], list_item['panel'])
        panel_text = main_page.get_faq_text(list_item['panel'])
        assert is_opened_faq and panel_text == list_item['text']

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()