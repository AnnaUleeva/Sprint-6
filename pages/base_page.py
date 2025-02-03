import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокрутка до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Прокрутка до элемента по локатору')
    def scroll_to_element_by_locator(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Нажатие на элемент')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Ожидание видимости элемента')
    def wait_visible_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Нажатие кнопки "Заказать" в хедере')
    def click_header_order_button(self):
        self.click_element(BasePageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Добавить значение в инпут')
    def send_keys(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step('Ожидание url')
    def wait_loading_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Проверка совпадения url с открытым')
    def check_url(self, url):
        self.wait_loading_url(url)
        assert self.driver.current_url == url

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Нажатие логотипа "Самокат" и проверка url')
    def click_scooter_logo_with_check(self):
        self.click_element(BasePageLocators.HEADER_SCOOTER_LINK)
        self.check_url(Constants.BASE_URL)

    @allure.step('Нажатие логотипа "Яндекс" и проверка url')
    def click_yandex_logo_with_check(self):
        self.click_element(BasePageLocators.HEADER_YANDEX_LINK)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.check_url(Constants.YANDEX_URL)