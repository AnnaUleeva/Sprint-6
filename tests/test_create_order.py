import allure

import pytest
from selenium import webdriver

from constants import Constants
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestCreateOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка создания заказа')
    @allure.description('Переходим к созданию азаказа, заполняем два шага с формами, проверяем что заказ создался' )
    @pytest.mark.parametrize('user_data, order_data', [
        [Constants.UserData['user_1'], Constants.OrderData['order_1']],
        [Constants.UserData['user_2'], Constants.OrderData['order_2']]
    ])
    def test_create_order(self, user_data, order_data):
        self.driver.get(Constants.BASE_URL)

        base_page = BasePage(self.driver)
        order_page = OrderPage(self.driver)

        base_page.click_header_order_button()
        order_page.set_personal_data(user_data)
        order_page.set_rent_data(order_data)

        order_page.confirm_create_order()
        order_page.close_modal_success_create_order()
        order_page.check_created_order()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()