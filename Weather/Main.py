import requests

from token_key import token_key


def get_weather(city, token_key):
    try:
        request_link = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_key}&units=metric")
        data = request_link.json()

        # """получаем название города"""
        city = data["name"]

        # """Текущая погода"""
        current_weather = data["main"]["temp"]

        # """Влажность воздуха"""
        air_humidity = data["main"]["humidity"]

        # """Скорость ветра"""
        Wind_speed = data["wind"]["speed"]
        print(
            f"Ваш город {city}\nТемпература {current_weather}°C\nВлажность воздуха {air_humidity}%\nСкорость ветра {Wind_speed} м/с")

    except Exception as ex:
        print(ex)
        print("Неверное название города")


def maim():
    city = str(input("Ведите город: "))
    get_weather(city, token_key)


maim()
