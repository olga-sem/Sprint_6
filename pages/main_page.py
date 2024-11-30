from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


@allure.title('Методы для проверки вопросов-ответов')
class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_the_question(self, num):
        locator_question_formated = self.format_locators(MainPageLocators.QUESTION_BUTTON, num)
        self.scroll_to_element(MainPageLocators.THE_LAST_QUESTION)
        self.click_the_element(locator_question_formated)

    @allure.step('Получение ответа')
    def get_the_answer(self, num):
        locator_answer_formated = self.format_locators(MainPageLocators.ANSWER_AREA, num)
        return self.get_text_from_element(locator_answer_formated)

    @allure.step('Проверка ответа на вопрос')
    def check_question_and_answer(self, num):
        self.click_the_question(num)
        return self.get_the_answer(num)

