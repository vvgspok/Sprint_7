## Описание
Данный файл содержит функции для класса CourierMethods, OrderMethods
Данный файл содержит тесты для класса TestCreateCouriers, TestLoginCouriers, TestCreateOrder, TestListOrder

## Функции для класса CourierMethods
### create_courier 
Создает курьера
### login_courier
Авторизует курьера в системе
### delete_courier
Удаляет курьера

## Функции для класса OrderMethods
### create_order
Создает заказ 
### get_orders
Получается список заказов 

## Тесты для класса TestCreateCouriers
### test_create_courier
Тест проверяет успешное создания курьера
### test_create_couriers_login_exists
Тест проверяет создание курьера с уже существующим логином 
### test_create_courier_without_required_field
Тест проверяет создание курьера без обязательного параметра логина или пароля 

## Тесты для класса TestLoginCouriers
### test_login_courier
Тест проверяет успешную авторизацию курьера в системе
### test_login_courier_without_required_fields
Тест проверяет получение ошибки при авторизации курьера без обязательного параметра логина или пароля
### test_login__courier_non_existent_courier
Тест проверяет получения ошибки при авторизации несуществующего курьера

## Тесты для класса class TestCreateOrder:
### test_create_orders 
Тест проверяет создания заказа с разными цветами

## Тесты для класса class TestListOrder:
### test_get_orders_list
Тест проверяет получение списка заказов 