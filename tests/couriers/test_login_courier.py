from methods.couriers_method import CourierMethods
import pytest
from data import COURIER_RESPONSE_ID, LOGIN_COURIERS_RESPONSE, couriers_data_without_login, couriers_data_without_pass, couriers_data_non_existent
from conftest import authorization_courier
import allure

@allure.feature('Авторизация курьера')
class TestLoginCouriers:

    @allure.title('Успешная авторизации курьера в системе')
    def test_login_courier(self, authorization_courier):
        response = authorization_courier
        courier_id = response.json()['id']
        assert response.status_code == 200 and response.text == COURIER_RESPONSE_ID.format(courier_id)

    @pytest.mark.parametrize(
        'params',
        [
            couriers_data_without_login,
            couriers_data_without_pass
        ]
    )

    @allure.title('Получения ошибки при авторизации курьера без логина или пароля')
    def test_login_courier_without_required_fields(self, params):
        courire_data = CourierMethods().login_courier(params)
        assert courire_data.status_code == 400 and courire_data.text == LOGIN_COURIERS_RESPONSE[1]

    @allure.title('Получения ошибки при авторизации несуществующего курьера')
    def test_login_courier_non_existent_courier(self):
        courier_data = CourierMethods().login_courier(couriers_data_non_existent)
        assert courier_data.status_code == 404 and courier_data.text == LOGIN_COURIERS_RESPONSE[2]

