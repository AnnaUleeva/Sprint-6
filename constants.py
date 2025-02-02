from locators.order_page_locators import OrderPagesLocators

class Constants:
    # Базовый url
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    # Раздел "Заказать"
    LINK_ORDER = "order"

    # Ссылка яндекс
    YANDEX_URL = "https://dzen.ru/?yredirect=true"

    # Данные для ввода персональных данных
    UserData = {
        "user_1": {
            "name": "Джон",
            "surname": "Доу",
            "address": "Адмиралтейская 8",
            "phone": "89991342454",
            "metro_index": 0
        },
        "user_2": {
            "name": "Джейн",
            "surname": "Смит",
            "address": "Пушкина 4, кв. 8",
            "phone": "+79008887733",
            "metro_index": 100
        }
    }

    # Данные для ввода данных аренды
    OrderData = {
        "order_1": {
            "delivery_day_after": 0,
            "scooter_color": [OrderPagesLocators.checkbox_scooter_color_grey, OrderPagesLocators.checkbox_scooter_color_black],
            "count_days_index": 0,
            "comment": "Какой-то комментарий"
        },
        "order_2": {
            "delivery_day_after": 3,
            "scooter_color": [OrderPagesLocators.checkbox_scooter_color_black],
            "count_days_index": 6,
            "comment": "Какой-то очень-очень-очень ддлииииииииииииииииииинный комментарий"
        }
    }