from methods.couriers_method import CourierMethods
import pytest
from data import couriers_existing, couriers_data_without_pass, couriers_data_without_login, CREATE_COURIERS_RESPONSE
from conftest import courier
import allure

@allure.feature('Создание курьера')
class TestCreateCouriers:

    @allure.title('Успешное создание заказа')
    def test_create_courier(self, courier):
        assert courier[1] == 201 and courier[2] == CREATE_COURIERS_RESPONSE[0]

    @allure.title('Получение ошибки при создании дубликата курьера')
    def test_create_couriers_login_exists(self):
        courire_data = CourierMethods().create_courier(couriers_existing)
        assert courire_data.status_code == 409 and courire_data.text == CREATE_COURIERS_RESPONSE[1]

    @pytest.mark.parametrize(
        'params',
        [
            couriers_data_without_login,
            couriers_data_without_pass
        ]
    )
    @allure.title('Получения ошибки при создании курьера без логина или пароля')
    def test_create_courier_without_required_field(self,params):
        courire_data = CourierMethods().create_courier(params)
        assert courire_data.status_code == 400 and courire_data.text == CREATE_COURIERS_RESPONSE[2]