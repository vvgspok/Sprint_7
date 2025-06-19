from methods.couriers_method import CourierMethods
import pytest
from data import COURIER_RESPONSE_ID, LOGIN_COURIERS_RESPONSE, couriers_data_without_login, couriers_data_without_pass, couriers_data_non_existent
from conftest import courier
import allure

@allure.feature('Авторизация курьера')
class TestLoginCouriers:

    @allure.title('Успешная авторизации курьера в системе')
    def test_login_courier(self, courier):
        courier_id = courier[0].json()['id']
        assert courier[0].status_code == 200 and courier[0].text == COURIER_RESPONSE_ID.format(courier_id)

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
        courire_data = CourierMethods().login_courier(couriers_data_non_existent)
        assert courire_data.status_code == 404 and courire_data.text == LOGIN_COURIERS_RESPONSE[2]

