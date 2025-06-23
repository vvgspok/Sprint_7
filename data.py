BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/"
ORDERS_URL = "orders/"
COURIERS_URL = "courier/"

couriers_existing = {
            "login": 'testloginvolkov',
            "password": 'testpassvolkov'
        }

couriers_data_without_login = {
    "login": "",
    "password": 'password'
}

couriers_data_without_pass = {
    "login": 'testloginvolkov',
    "password": ""
}

couriers_data_non_existent = {
    "login": 'testnon_existent',
    "password": 'testnon_existent'
}

color = [
    ['BLACK'],
    ['GREY']
]

CREATE_COURIERS_RESPONSE = [
    '{"ok":true}',
    '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}',
    '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
]

LOGIN_COURIERS_RESPONSE = [
    '{"id":547518}',
    '{"code":400,"message":"Недостаточно данных для входа"}',
    '{"code":404,"message":"Учетная запись не найдена"}'
]

COURIER_RESPONSE_ID = '{{"id":'"{}"'}}'
ORDER_RESPONSE_TRACK = '{{"track":'"{}"'}}'

ORDER_DATA_1 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}

ORDER_DATA_2 = {
    "firstName": "Sasuke",
    "lastName": "Uchiha",
    "address": "Orochimaru's Hideout",
    "metroStation": 2,
    "phone": "+7 900 222 22 22",
    "rentTime": 2,
    "deliveryDate": "2023-07-02",
    "comment": "Searching for Itachi",
    "color": ["GREY"]
}

ORDER_DATA_3 = {
    "firstName": "Kakashi",
    "lastName": "Hatake",
    "address": "Hokage's office",
    "metroStation": 3,
    "phone": "+7 900 333 33 33",
    "rentTime": 3,
    "deliveryDate": "2023-07-03",
    "comment": "Reading Make-Out Paradise",
    "color": ["BLACK", "GREY"]
}

ORDER_DATA_4 = {
    "firstName": "Sakura",
    "lastName": "Haruno",
    "address": "Konoha Hospital",
    "metroStation": 5,
    "phone": "+7 900 444 44 44",
    "rentTime": 4,
    "deliveryDate": "2023-07-04",
    "comment": "Medical ninjutsu training",
    "color": []
}