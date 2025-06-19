import requests
import allure
from data import BASE_URL, ORDERS_URL

class OrderMethods:

    @allure.step('Создание заказа')
    def create_order(self, params=None):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=params)
        return response

    @allure.step('Получение списка заказов')
    def get_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.text