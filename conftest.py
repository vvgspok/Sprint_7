import pytest
from helpers import generate_couriers_data
from methods.couriers_method import CourierMethods

@pytest.fixture
def courier():
    courier_data = generate_couriers_data()
    response = CourierMethods().create_courier(courier_data)
    id_courier = CourierMethods().login_courier(courier_data)
    yield id_courier, response.status_code, response.text, courier_data
    CourierMethods().delete_courier(id_courier.json()['id'])

