import requests
import config_2
import data_2


def create_order():
    """Создание заказа."""
    return requests.post(
        f"{config_2.URL_SERVICE}{config_2.CREATE_ORDER_PATH}",
        json=data_2.order_body,
        headers=data_2.headers,
        timeout=10
    )


def get_order_by_track(track):
    """Получение заказа по треку."""
    return requests.get(
        f"{config_2.URL_SERVICE}{config_2.GET_ORDER_PATH}",
        params={"t": track},
        timeout=10
    )