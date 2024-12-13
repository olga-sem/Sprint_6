import allure
from pages.switching_pages import SwitchingPages


@allure.title('Тесты на переходы по лого')
class TestSwitchingPages:

    @allure.description('Тест на переход на страницу Дзен по клику на лого Яндекс в шапке приложения ЯндексСамокат')
    def test_check_yandex_logo(self, driver):
        switching_pages = SwitchingPages(driver)
        assert switching_pages.check_yandex_logo() == "Найти"

    @allure.description('Тест на переход на главную станицу приложения по клику на лого Самокат в шапке приложения ЯндексСамокат')
    def test_check_scooter_logo(self, driver):
        switching_pages = SwitchingPages(driver)
        assert switching_pages.check_scooter_logo() == "Заказать"
