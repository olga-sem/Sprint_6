from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


@allure.title('Методы для создания заказа')
class OrderPage(BasePage):

    @allure.step('Оформление заказа')
    def set_the_order(self, name, last_name, address, metro_station, phone, date, duration, color):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_the_element(OrderPageLocators.METRO_STATION_FIELD)
        self.click_the_element(metro_station)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, phone)
        self.click_the_element(OrderPageLocators.NEXT_BUTTON)
        self.add_text_to_element(OrderPageLocators.DATE_FIELD, date)
        self.click_the_element(OrderPageLocators.ORDER_HEADER)
        self.click_the_element(OrderPageLocators.DURATION_FIELD)
        self.click_the_element(duration)
        self.click_the_element(color)
        self.click_the_element(OrderPageLocators.ORDER_BUTTON_ORDER_PAGE)
        self.find_element_with_wait(OrderPageLocators.YES_BUTTON)
        self.click_the_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверка создания заказа')
    def check_the_order(self):
        return self.get_text_from_element(OrderPageLocators.CHECK_BUTTON)