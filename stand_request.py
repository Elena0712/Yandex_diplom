import requests
import config
import data

# Создаём заказ
response = requests.post(
    f"{config.URL_SERVICE}{config.CREATE_ORDER_PATH}",
    json=data.order_body,
    headers=data.headers,
    timeout=10
)

print("POST /orders статус:", response.status_code)
print("Тело ответа:", response.text)

# Если заказ создан успешно
if response.status_code == 201:
    resp_json = response.json()
    track = resp_json.get("track")
    if not track:
        print("Ошибка: трек не вернулся")
    else:
        print("Трек заказа:", track)

        # Получаем заказ по треку
        get_response = requests.get(
            f"{config.URL_SERVICE}{config.GET_ORDER_PATH}",
            params={"t": track},
            timeout=10
        )
        print("GET /orders/track статус:", get_response.status_code)
        print("Тело ответа GET:", get_response.text)

        if get_response.status_code == 200:
            print("Заказ успешно получен по треку!")
        else:
            print("Ошибка при получении заказа по треку.")
else:
    print("Ошибка при создании заказа. Код:", response.status_code)