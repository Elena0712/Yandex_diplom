# Yandex_diplom

Проект автотестов для сервиса заказов самокатов.

---

## 📂 Структура проекта

- config_2.py — настройки URL и путей  
- data_2.py — тело запроса и заголовки  
- sender_stand_request_2.py — функции для отправки запросов  
- create_scooter_test_2.py — тесты (pytest)  
- README.md — описание проекта  

---

## 🛠 Требуемые пакеты

Для работы проекта необходимы:  

- Python 3.10+  
- pytest  
- requests  

Установка зависимостей (в активированном виртуальном окружении):
pip install requests
python -m pytest create_scooter_test_2.py -v -s #запуск теста