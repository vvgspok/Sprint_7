import pytest
from helpers import generate_couriers_data
from methods.couriers_method import CourierMethods

@pytest.fixture
def courier():
    courier_data = generate_couriers_data()
    response = CourierMethods().create_courier(courier_data)
    yield response, courier_data
    id_courier = CourierMethods().login_courier(courier_data)
    CourierMethods().delete_courier(id_courier.json()['id'])

@pytest.fixture
def authorization_courier(courier):
    response = CourierMethods().login_courier(courier[1])
    return response