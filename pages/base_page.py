from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.title('Базовые методы')
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_the_element(self, locator):
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавление текста к элементу')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста с элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Форматирование локаторов')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        locator = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    @allure.step('Переход на другую страницу')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])