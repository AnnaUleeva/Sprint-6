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
        self.send_keys(OrderPagesLocators.input_name, user['name'])
        self.send_keys(OrderPagesLocators.input_surname, user['surname'])
        self.send_keys(OrderPagesLocators.input_address, user['address'])
        self.click_element(OrderPagesLocators.input_metro)
        self.click_element_in_list(OrderPagesLocators.select_metro_item, user['metro_index'])
        self.send_keys(OrderPagesLocators.input_phone, user['phone'])
        self.click_element(OrderPagesLocators.next_button)

    @allure.step('Заполнение данных аренды')
    def set_rent_data(self, order):
        self.wait_visible_element(OrderPagesLocators.order_header)
        self.click_element(OrderPagesLocators.input_rental_period)
        self.click_element_in_list(OrderPagesLocators.input_rental_period_option, order['count_days_index'])
        delivery_date = (date.today() + timedelta(days=order['delivery_day_after'])).strftime('%d.%m.%Y')
        self.send_keys(OrderPagesLocators.input_delivery_date, delivery_date)
        self.click_checkboxes(order['scooter_color'])
        self.send_keys(OrderPagesLocators.input_comment, order['comment'])
        self.click_element(OrderPagesLocators.submit_button)

    @allure.step('Подтверждение создания заказа')
    def confirm_create_order(self):
        self.wait_visible_element(OrderPagesLocators.modal_submit_header)
        self.click_element(OrderPagesLocators.modal_submit_ok_button)

    @allure.step('Закрытие модального окна об успешном создании заказа')
    def close_modal_success_create_order(self):
        self.wait_visible_element(OrderPagesLocators.modal_success_header)
        self.click_element(OrderPagesLocators.modal_success_show_status_button)

    @allure.step('Проверка перехода к созданному заказу')
    def check_created_order(self):
        self.wait_visible_element(OrderPagesLocators.order_cancel_button)
        assert self.find_element(OrderPagesLocators.order_cancel_button).is_displayed()

    @allure.step('Проверка url на соответствие странице создания заказа')
    def check_order_page_url(self):
        self.check_url(f"{Constants.BASE_URL}{Constants.LINK_ORDER}")

