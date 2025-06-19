from data import BASE_URL, COURIERS_URL
import requests
import allure
from helpers import generate_couriers_data

class CourierMethods:

    @allure.step('Создание курьера')
    def create_courier(self, params=None):
        if params is None:
            params = generate_couriers_data()
        response = requests.post(
            f'{BASE_URL}{COURIERS_URL}',
            data=params
        )
        return response

    @allure.step('Авторизация курьера в системе')
    def login_courier(self, params):
        response = requests.post(
            f'{BASE_URL}{COURIERS_URL}login',
            data=params
        )
        return response

    @allure.step('Удаление курьера')
    def delete_courier(self, id):
        response = requests.delete(
            f'{BASE_URL}{COURIERS_URL}{id}'
        )
        return response

