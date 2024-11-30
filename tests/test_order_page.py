import allure
import pytest

from locators.order_page_locators import OrderPageLocators
import data
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title('Тесты на оформление заказа')
class TestOrderPage:

     @allure.description('Тест на оформление заказа по разным кнопкам Заказать')
     @pytest.mark.parametrize(
         'locator, name, last_name, address, metro_station, phone, date, duration, color',
          [
              (MainPageLocators.ORDER_UPPER_BUTTON, data.name_1, data.last_name_1, data.address_1, OrderPageLocators.LUBYANKA_STATION, data.phone_1, data.date_1, OrderPageLocators.TWO_DAYS_DURATION, OrderPageLocators.BLACK_COLOR),
              (MainPageLocators.ORDER_LOWER_BUTTON, data.name_2, data.last_name_2, data.address_2, OrderPageLocators.SOKOLNIKI_STATION, data.phone_2, data.date_2, OrderPageLocators.FIVE_DAYS_DURATION, OrderPageLocators.GREY_COLOR)
          ]
     )
     def test_create_order(self, driver, locator, name, last_name, address, metro_station, phone, date, duration, color):
         main_page = MainPage(driver)
         order_page = OrderPage(driver)
         main_page.click_the_element(locator)
         order_page.set_the_order(name, last_name, address, metro_station, phone, date, duration, color)
         assert order_page.check_the_order() == "Посмотреть статус"