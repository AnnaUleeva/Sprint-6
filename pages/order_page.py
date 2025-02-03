from datetime import date, timedelta

import allure

from constants import Constants
from locators.order_page_locators import OrderPagesLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажатие на элемент списка')
    def click_element_in_list(self, locator, index):
        try:
            self.wait_visible_element(locator)
            elements = self.find_elements(locator)
            if len(elements) < index:
                raise IndexError(f"Необходимо указать индекс в диапасоне 0-{len(elements)-1}")
            element = elements[index]
            self.scroll_to_element(element)
            element.click()
        except Exception as e:
            print(f"{type(e).__name__} - {e}")

    @allure.step('Нажатие чекбоксов')
    def click_checkboxes(self, locators):
        for locator in locators:
             self.click_element(locator)

    @allure.step('Заполнение персональных данных')
    def set_personal_data(self, user):
        self.send_keys(OrderPagesLocators.INPUT_NAME, user['name'])
        self.send_keys(OrderPagesLocators.INPUT_SURNAME, user['surname'])
        self.send_keys(OrderPagesLocators.INPUT_ADDRESS, user['address'])
        self.click_element(OrderPagesLocators.INPUT_METRO)
        self.click_element_in_list(OrderPagesLocators.SELECT_METRO_ITEM, user['metro_index'])
        self.send_keys(OrderPagesLocators.INPUT_PHONE, user['phone'])
        self.click_element(OrderPagesLocators.NEXT_BUTTON)

    @allure.step('Заполнение данных аренды')
    def set_rent_data(self, order):
        self.wait_visible_element(OrderPagesLocators.ORDER_HEADER)
        self.click_element(OrderPagesLocators.INPUT_RENTAL_PERIOD)
        self.click_element_in_list(OrderPagesLocators.INPUT_RENTAL_PERIOD_OPTION, order['count_days_index'])
        delivery_date = (date.today() + timedelta(days=order['delivery_day_after'])).strftime('%d.%m.%Y')
        self.send_keys(OrderPagesLocators.INPUT_DELIVERY_DATE, delivery_date)
        self.click_checkboxes(order['scooter_color'])
        self.send_keys(OrderPagesLocators.INPUT_COMMENT, order['comment'])
        self.click_element(OrderPagesLocators.SUBMIT_BUTTON)

    @allure.step('Подтверждение создания заказа')
    def confirm_create_order(self):
        self.wait_visible_element(OrderPagesLocators.MODAL_SUBMIT_HEADER)
        self.click_element(OrderPagesLocators.MODAL_SUBMIT_OK_BUTTON)

    @allure.step('Закрытие модального окна об успешном создании заказа')
    def close_modal_success_create_order(self):
        self.wait_visible_element(OrderPagesLocators.MODAL_SUCCESS_HEADER)
        self.click_element(OrderPagesLocators.MODAL_SUCCESS_SHOW_STATUS_BUTTON)

    @allure.step('Проверка перехода к созданному заказу')
    def check_created_order(self):
        self.wait_visible_element(OrderPagesLocators.ORDER_CANCEL_BUTTON)
        assert self.find_element(OrderPagesLocators.ORDER_CANCEL_BUTTON).is_displayed()

    @allure.step('Проверка url на соответствие странице создания заказа')
    def check_order_page_url(self):
        self.check_url(f"{Constants.BASE_URL}{Constants.LINK_ORDER}")

