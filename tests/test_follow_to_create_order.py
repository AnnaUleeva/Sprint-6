import allure
from selenium import webdriver

from constants import Constants
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestFollowToCreateOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка перехода по кнопке в хедере')
    @allure.description('Кликаем по кнопке, проверяем что перешли на нужный url')
    def test_follow_by_header_button(self):
        self.driver.get(Constants.BASE_URL)
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        main_page.click_header_order_button()
        order_page.check_order_page_url()

    @allure.title('Проверка перехода по кнопке на главной странице')
    @allure.description('Скролим до нужной кнопки, кликаем, проверяем что перешли на нужный url')
    def test_follow_page_button(self):
        self.driver.get(Constants.BASE_URL)
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        main_page.click_order_button()
        order_page.check_order_page_url()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()