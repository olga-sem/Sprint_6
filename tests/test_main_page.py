import allure
import pytest

from pages.main_page import MainPage
import data


@allure.title('Тесты на вопросы и ответы')
class TestMainPage:

    @allure.description('Тест на соответствие ответа вопросу')
    @pytest.mark.parametrize('num, answer', enumerate(data.FAQ))
    def test_questions_and_answers(self, driver, num, answer):
        main_page = MainPage(driver)
        assert main_page.check_question_and_answer(num) == answer
