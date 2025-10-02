import sender_stand_request_2

def test_create_and_get_order():
    # Создание заказа
    response = sender_stand_request_2.create_order()
    print("POST /orders статус:", response.status_code)
    print("Тело ответа:", response.text)
    assert response.status_code == 201, (
        f"Ошибка при создании заказа: {response.status_code}, {response.text}"
    )
# Казимова Елена, 34-я когорта — Финальный проект. Инженер по тестированию плюс
    resp_json = response.json()
    track = resp_json.get("track")
    assert track, "Ошибка: трек не вернулся в ответе"
    print("Трек заказа:", track)

    # Получение заказа по треку
    get_response = sender_stand_request_2.get_order_by_track(track)
    print("GET /orders/track статус:", get_response.status_code)
    print("Тело ответа GET:", get_response.text)
    assert get_response.status_code == 200, (
        f"Ошибка при получении заказа: {get_response.status_code}, {get_response.text}"
    )

    # Проверка, что имя в заказе совпадает с ожидаемым
    order_data = get_response.json()
    assert order_data["order"]["firstName"] == "Роман", (
        f"Имя в заказе некорректное: {order_data}"
    )