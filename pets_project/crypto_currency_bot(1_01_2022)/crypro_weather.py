import json
import requests
import random
import datetime


def get_weather(city):
    print(city)

    open_weather_token = "*****************"
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Raine": "Дождь: \U00002614",
        "Drizzle": "Дождь: \U00002614",
        "Thunderstorm": "Гроза: \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # command = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Лучше сам посмотри что там)"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        text = ""
        text += (  # f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}°С {wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"Хорошее настроение всегда должно быть с тобой - погода, не решает!")
        return text

    except:
        return {
            'Некорректное название города',
            # 'body': json.dumps('Hello from Lambda Sir!')
        }


TELE_TOKEN = "*****************:*****************-*****************"
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)


def get_data():
    url = 'https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD,tETHUSD,tETCUSD,tDOGE:USD,tSUSHI:USD,tDOTUSD,tVETUSD,tXRPUSD,tADAUSD'
    r = requests.get(url)
    r = r.json()
    text = ""
    for i in r:
        if i[6] * 100 >= 0:
            text += (f"🟢{i[0][1:4]} | ${round(i[1], 2)} | {(round(i[6] * 100, 2))}%\n")
        else:
            text += (f"🔴{i[0][1:4]} | ${round(i[1], 2)} | {(round(i[6] * 100, 2))}%\n")
    return text


def send_message(text, chat_id):
    final_text = text
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=HTML".format(final_text, chat_id)
    requests.get(url)


def lambda_handler(event, context):
    print(event['body'])
    # TODO implement
    message = json.loads(event['body'])

    try:

        chat_id = message['message']['chat']['id']
        command = message['message']['text']
        user_name = message['message']['chat']["first_name"]
        duble_text = ["Жребий брошен",
                      "Ни дня без штриха, ни дня без строчки",
                      "Ничего уже не говорят такого, чего не было сказано раньше",
                      "Никакая опасность не преодолевается без риска",
                      "О времена, о нравы!",
                      "Равное равному воздается",
                      "Началo — половина всего", "Сколько людей, столько мнений", "Для понимающего достаточно"]

        if command == "/price":
            text = str(get_data())
        elif command == "/start":
            text = f"Привет {user_name} теперь все мета-даные у нас) нажми меню чтобы узнать команды"



        elif "/weather" in command:
            city = []
            for i in command.split():
                city.append(i)
            print(city)
            text = str(get_weather(city[1]))



        else:
            text = "Problem with command"
        send_message(text, chat_id)
        # send_message(str(random.choice(duble_text)), chat_id)
        return {
            'statusCode': 200,
            # 'body': json.dumps('Hello from Lambda Sir!')
        }

    except:
        return {
            'statusCode': 200,
            # 'body': json.dumps('Hello from Lambda Sir!')
        }
