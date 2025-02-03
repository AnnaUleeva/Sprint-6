import allure
from selenium import webdriver

from constants import Constants
from pages.base_page import BasePage

class TestFollowToLogo:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка перехода по логотипу "Самокат"')
    @allure.description('Находясь на странице зказа, кликаем по логотипу, проверяем что перешли на главную страницу')
    def test_follow_to_scooter_logo(self):
        self.driver.get(f"{Constants.BASE_URL}{Constants.LINK_ORDER}")
        base_page = BasePage(self.driver)
        base_page.click_scooter_logo_with_check()

    @allure.title('Проверка перехода по логотипу "Яндекс"')
    @allure.description('Находясь на главной странице, кликаем по логотипу, проверяем что перешли на страницу дзена')
    def test_follow_to_yandex_logo(self):
        self.driver.get(Constants.BASE_URL)
        base_page = BasePage(self.driver)
        base_page.click_yandex_logo_with_check()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()