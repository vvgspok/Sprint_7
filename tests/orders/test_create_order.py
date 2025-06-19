from methods.order_methods import OrderMethods
from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4, ORDER_RESPONSE_TRACK
import pytest
import allure

@allure.feature('Создание заказов')
class TestCreateOrder:

    @pytest.mark.parametrize(
        'params',
        [
            ORDER_DATA_1,
            ORDER_DATA_2,
            ORDER_DATA_3,
            ORDER_DATA_4
        ]
    )
    @allure.title('Проверка создания заказа с разными цветами')
    def test_create_orders(self, params):
        list_orders = OrderMethods().create_order(params)
        order_tack = list_orders.json()['track']
        assert list_orders.status_code == 201 and list_orders.text == ORDER_RESPONSE_TRACK.format(order_tack)


