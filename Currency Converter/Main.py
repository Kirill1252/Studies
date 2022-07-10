import json

import requests


def get_currecy():
    currency = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    data = currency.json()
    # """Курс валют"""
    # """USD"""
    name_usd = data[0]["ccy"]
    # """Курс продажи"""
    name_sale_usd = data[0]["sale"]
    # """Курс покупки"""
    purchases_usd = data[0]["buy"]
    print(f"КУРС ВАЛЮТ\nДолар: {name_usd}\tКурс продажи: {name_sale_usd}\tКурс покупки: {purchases_usd}")

    # """EUR"""
    name_EUR = data[1]["ccy"]
    # """Курс продажи"""
    name_sale_EUR = data[1]["sale"]
    # """Курс покупки"""
    purchases_EUR = data[1]["buy"]
    print(f"Євро: {name_EUR}\tКурс продажи: {name_sale_EUR}\tКурс покупки: {purchases_EUR}")


# """Конвертер USD"""
def usd_purchases():
    # """Курс покупки"""
    currency = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    data = currency.json()
    summa = float(input("Сколько гривен вы хотите обменять на доллар: "))
    purchases_usd = json.loads(data[0]["buy"])
    sum_usd = summa / purchases_usd
    print(f"Вы купите: {sum_usd:.2f} $")


def usd_sale():
    currency = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    data = currency.json()
    summa = float(input("Сколько долларов вы хотите обменять на гривны: "))
    name_sale_usd = json.loads(data[0]["sale"])
    sum_usd = summa * name_sale_usd
    print(f"Вы купите: {sum_usd:.2f} гривен")


# """Конвертер EUR"""
def EUR_purchases():
    # """Курс покупки"""
    currency = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    data = currency.json()
    summa = float(input("Сколько гривен вы хотите обменять на Євро: "))
    purchases_EUR = json.loads(data[1]["buy"])
    sum_EUR = summa / purchases_EUR
    print(f"Вы купите: {sum_EUR:.2f} Евро")


def EUR_sale():
    currency = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    data = currency.json()
    summa = float(input("Сколько Євро вы хотите обменять на гривны: "))
    name_sale_EUR = json.loads(data[1]["sale"])
    sum_EUR = summa * name_sale_EUR
    print(f"Вы купите: {sum_EUR:.2f} гривен")


def main():
    get_currecy()
    try:
        print("""
                Долар--USD
                Євро--EUR
                    """)
        currency = input("Какая валюта вас интересует?")
        if currency == "USD":
            a_USD = int(input("Чтобы купить введите '1'\tЧтобы продать ввудите '2':"))
            if a_USD == 1:
                usd_purchases()
            else:
                usd_sale()
        elif currency == "EUR":
            a_EUR = int(input("Чтобы купить введите '1'\tЧтобы продать ввудите '2':"))
            if a_EUR == 1:
                EUR_purchases()
            else:
                EUR_sale()
        elif currency == "RUR":
            a_RUR = int(input("Чтобы купить введите '1'\tЧтобы продать ввудите '2':"))
            if a_RUR == 1:
                EUR_purchases()
            else:
                EUR_sale()

    except Exception as ex:
        print(ex)
        print("Неверное ввод")


main()
