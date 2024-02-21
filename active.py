from pymino import Client
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("""
▄▀█ █▀▀ ▀█▀ █ █░█ █▀▀ ░ █▀█ █▄█|ᵇʸ ᵈᵉˡᵃᶠᵃᵘˡᵗ
█▀█ █▄▄ ░█░ █ ▀▄▀ ██▄ ▄ █▀▀ ░█░
""")

def gd_print(value):
    green_color = '\033[32m'
    reset_color = '\033[0m'
    result = f"\n>{green_color} {value} {reset_color}\n"
    print(result)

def bd_print(value):
    red_color = '\033[31m'
    reset_color = '\033[0m'
    result = f"\n>{red_color} {value} {reset_color}\n"
    print(result)

def main():
    while True:
        try:
            clientz = Client(signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44", device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9") #proxy = "http://user126128:5yrioa@84.32.15.126:3014") - использовать прокси при желании
            clientz.login(email = input("E-mail: "), password = input("Пароль: "))
            gd_print(f"Вошли в аккаунт '{clientz.profile.username}'")
            break
        except Exception as error:
            bd_print(f"Ошибка: {error}")

    while True:
        try:
            comId = clientz.fetch_community_id(community_link = input("Ссылка на сообщество: "))
            clientz.set_community_id(community_id=comId)
            gd_print(f"Получили информацию о сообществе '{comId}'")
            break
        except Exception as error:
            bd_print(f"Ошибка: {error}")

    while True:
        try:
            start_time = int(time.time())
            end_time = start_time + 300
            clientz.community.send_active(start=start_time, end=end_time)
            gd_print("Отправили активность за 5 минут.")
        except Exception as error:
            bd_print(f"Не удалось отправить активность: {error}")

        time.sleep(300)


if __name__ == '__main__':
    main()
    print("\nСкрипт завершил свою работу.")
