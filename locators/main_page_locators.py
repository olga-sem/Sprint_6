from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIES_BUTTON = By.XPATH, '//button[@id="rcc-confirm-button"]'
    ORDER_UPPER_BUTTON = By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Заказать"]'
    ORDER_LOWER_BUTTON = By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle") and text()="Заказать"]'
    QUESTION_BUTTON = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_AREA = By.XPATH, '//*[@id="accordion__panel-{}"]'
    THE_LAST_QUESTION = By.XPATH, '//div[@id="accordion__heading-7"]'
    FAQ_LINE = By.XPATH, '//div[text()="Вопросы о важном"]'