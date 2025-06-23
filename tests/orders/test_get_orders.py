from methods.order_methods import OrderMethods
import pytest
import allure

@allure.feature('Список заказов')
class TestListOrder:

    @allure.title('Получение список заказов')
    def test_get_orders_list(self):
        list_orders = OrderMethods().get_orders()
        assert list_orders[0] == 200 and list_orders[1] != []

