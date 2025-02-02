from selenium.webdriver.common.by import By


class OrderPagesLocators:
    # Инпут имени формы ввода персональных данных
    input_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    # Инпут фамилии формы ввода персональных данных
    input_surname = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    # Инпут адреса формы ввода персональных данных
    input_address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    # Инпут метро формы ввода персональных данных
    input_metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # Элемент выпадающего списка метро формы ввода персональных данных
    select_metro_item = (By.XPATH, ".//div[@class='select-search__select']//li[@class='select-search__row']")
    # Инпут номера телефона формы ввода персональных данных
    input_phone = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее" формы ввода персональных данных
    next_button = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")

    # Заголовок формы ввода данных аренды
    order_header = (By.XPATH, ".//div[text()='Про аренду' and @class='Order_Header__BZXOb']")
    # Инпут даты доставки формы ввода данных аренды
    input_delivery_date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    # Инпут срока аренды из формы ввода данных аренды
    input_rental_period = (By.XPATH, ".//div[@class='Dropdown-control']")
    # Элемент выпадающего списка срока арнеды из формы ввода данных аренды
    input_rental_period_option = (By.XPATH, ".//div[@class='Dropdown-option']")
    # Чекбокс цвета самоката - черный формы ввода данных аренды
    checkbox_scooter_color_black = (By.XPATH, ".//div[text()='Цвет самоката']/following-sibling::label[@for='black']")
    # Чекбокс цвета самоката - серый формы ввода данных аренды
    checkbox_scooter_color_grey = (By.XPATH, ".//div[text()='Цвет самоката']/following-sibling::label[@for='grey']")
    # Инпут комментария формы ввода данных аренды
    input_comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Заказать" формы ввода данных аренды
    submit_button = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Заголовок модального окна подтверждения создания заказа
    modal_submit_header = (By.XPATH, ".//div[text()='Хотите оформить заказ?' and @class='Order_ModalHeader__3FDaJ']")
    # Кнопка подтверждения создания заказа
    modal_submit_ok_button = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Да']")

    # Заголовок модального окна успешного создания заказа
    modal_success_header = (By.XPATH, ".//div[text()='Заказ оформлен' and @class='Order_ModalHeader__3FDaJ']")
    # Кнопка "Посмотреть статус" в модальном окне успешного создания заказа
    modal_success_show_status_button = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']//button[text()='Посмотреть статус']")

    # Кнопка "Отменить заказ" на странице заказа
    order_cancel_button = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Отменить заказ']")
