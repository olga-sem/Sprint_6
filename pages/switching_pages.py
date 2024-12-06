from locators.dzen_locators import DzenLocators
from locators.main_page_locators import MainPageLocators
from locators.switching_pages_locators import SwitchingPagesLocators
from pages.base_page import BasePage
import allure


@allure.title('Методы для проверки переходов по лого')
class SwitchingPages(BasePage):


     def check_yandex_logo(self):
        self.click_the_element(MainPageLocators.COOKIES_BUTTON)
        self.click_the_element(SwitchingPagesLocators.YANDEX_LOGO)
        self.switch_to_window()
        self.find_element_with_wait(DzenLocators.SEARCH_BUTTON)
        return self.get_text_from_element(DzenLocators.SEARCH_BUTTON)

     @allure.step('Проверка перехода на главную страницу Самоката')
     def check_scooter_logo(self):
        self.click_the_element(MainPageLocators.COOKIES_BUTTON)
        self.click_the_element(MainPageLocators.ORDER_UPPER_BUTTON)
        self.click_the_element(SwitchingPagesLocators.SCOOTER_LOGO)
        self.scroll_to_element(MainPageLocators.ORDER_LOWER_BUTTON)
        return self.get_text_from_element(MainPageLocators.ORDER_LOWER_BUTTON)