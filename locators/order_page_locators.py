from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Имя"]'
    LAST_NAME_FIELD = By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Фамилия"]'
    ADDRESS_FIELD = By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION_FIELD = By.XPATH, '//input[@class="select-search__input" and @placeholder="* Станция метро"]'
    LUBYANKA_STATION = By.XPATH, './/*[contains(text(), "Лубянка")]'
    SOKOLNIKI_STATION = By.XPATH, './/*[contains(text(), "Сокольники")]'
    PHONE_FIELD = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'
    DATE_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    ORDER_HEADER = By.XPATH, '//div[contains(@class, "Order_Header") and text()="Про аренду"]'
    DURATION_FIELD = By.XPATH, '//*[@class="Dropdown-placeholder"]'
    TWO_DAYS_DURATION = By.XPATH, '//*[contains(text(), "двое суток")]'
    FIVE_DAYS_DURATION = By.XPATH, '//*[contains(text(), "пятеро суток")]'
    BLACK_COLOR = By.XPATH, '//input[@id="black"]'
    GREY_COLOR = By.XPATH, '//input[@id="grey"]'
    ORDER_BUTTON_ORDER_PAGE = By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle") and text()="Заказать"]'
    YES_BUTTON = By.XPATH, '//button[text()="Да"]'
    CHECK_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'