from selenium.webdriver.common.by import By


class OrderPagesLocators:
    # Инпут имени формы ввода персональных данных
    INPUT_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    # Инпут фамилии формы ввода персональных данных
    INPUT_SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    # Инпут адреса формы ввода персональных данных
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    # Инпут метро формы ввода персональных данных
    INPUT_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # Элемент выпадающего списка метро формы ввода персональных данных
    SELECT_METRO_ITEM = (By.XPATH, ".//div[@class='select-search__select']//li[@class='select-search__row']")
    # Инпут номера телефона формы ввода персональных данных
    INPUT_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее" формы ввода персональных данных
    NEXT_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")

    # Заголовок формы ввода данных аренды
    ORDER_HEADER = (By.XPATH, ".//div[text()='Про аренду' and @class='Order_Header__BZXOb']")
    # Инпут даты доставки формы ввода данных аренды
    INPUT_DELIVERY_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    # Инпут срока аренды из формы ввода данных аренды
    INPUT_RENTAL_PERIOD = (By.XPATH, ".//div[@class='Dropdown-control']")
    # Элемент выпадающего списка срока арнеды из формы ввода данных аренды
    INPUT_RENTAL_PERIOD_OPTION = (By.XPATH, ".//div[@class='Dropdown-option']")
    # Чекбокс цвета самоката - черный формы ввода данных аренды
    CHECKBOX_SCOOTER_COLOR_BLACK = (By.XPATH, ".//div[text()='Цвет самоката']/following-sibling::label[@for='black']")
    # Чекбокс цвета самоката - серый формы ввода данных аренды
    CHECKBOX_SCOOTER_COLOR_GREY = (By.XPATH, ".//div[text()='Цвет самоката']/following-sibling::label[@for='grey']")
    # Инпут комментария формы ввода данных аренды
    INPUT_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Заказать" формы ввода данных аренды
    SUBMIT_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Заголовок модального окна подтверждения создания заказа
    MODAL_SUBMIT_HEADER = (By.XPATH, ".//div[text()='Хотите оформить заказ?' and @class='Order_ModalHeader__3FDaJ']")
    # Кнопка подтверждения создания заказа
    MODAL_SUBMIT_OK_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Да']")

    # Заголовок модального окна успешного создания заказа
    MODAL_SUCCESS_HEADER = (By.XPATH, ".//div[text()='Заказ оформлен' and @class='Order_ModalHeader__3FDaJ']")
    # Кнопка "Посмотреть статус" в модальном окне успешного создания заказа
    MODAL_SUCCESS_SHOW_STATUS_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']//button[text()='Посмотреть статус']")

    # Кнопка "Отменить заказ" на странице заказа
    ORDER_CANCEL_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Отменить заказ']")
