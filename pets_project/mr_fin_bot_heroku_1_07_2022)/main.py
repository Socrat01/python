import os
import telebot
import logging
from telebot import types
from datetime import datetime, timedelta

import db
from config import *
from flask import Flask, request
import psycopg2
import helper as h

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.INFO)

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()


finta_dict = {}
class Finta:
    def __init__(self, suma):
        self.suma = suma
        self.category = None
        self.category_abstraction = None
        self.approved = None


def update_message_count(user_id):
    db_object.execute(f"UPDATE users SET messages = messages + 1 WHERE id_telegram = {user_id}")
    db_connection.commit()


@bot.message_handler(commands=["start"])
def start(message):

    user_id = message.from_user.id
    username = message.from_user.username
    bot.reply_to(message, f"Привіт {username}!")

    result = db.inspect(user_id)
    if not result:

        msg = bot.send_message(message.chat.id, f"⛔️Вас немає в базі\nДля продовження потрібно пройти реєстрацію\n📲➡️ /registration")
        bot.register_next_step_handler(msg, regestration)
        db.add_db(user_id, username)

    bot.send_message(message.chat.id, f"Ви є в базі✅")
    update_message_count(user_id)


@bot.message_handler(commands=['registration'])
def regestration(message):

    try:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Відправити номер телефону", request_contact=True)
        keyboard.add(button_phone)

        bot.send_message(message.chat.id, f'Натисніть кнопку для передачі номеру телефона ⬇️', reply_markup=keyboard)
        update_message_count(message.from_user.id)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Отримайте дозвіл від адміністратора')

@bot.message_handler(content_types=['contact'])
def contact(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    try:
        if message.contact is not None:
            bot.send_message(message.chat.id, f'Телефон добавлений в базу🤝', reply_markup=markup)
            db.phone(message.from_user.id, message.contact.phone_number)
            update_message_count(message.from_user.id)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'contact error')


@bot.message_handler(regexp="^[+]?[0-9]+$")
def getting_suma(message):

    try:
        logging.info("Initialization command contact")
        chat_id = message.chat.id
        suma = message.text
        finta = Finta(suma)
        finta_dict[chat_id] = finta

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Подключаем клавиатуру
        food = types.KeyboardButton(text="🍏продукти")
        utilities = types.KeyboardButton(text="🏠комунальні")
        cafe = types.KeyboardButton(text="☕️кафе")
        credit = types.KeyboardButton(text="💳кредити")
        dpay = types.KeyboardButton(text="💰+витрати")
        invest = types.KeyboardButton(text="📊інвестиції")

        keyboard.add(food, utilities, cafe, credit, dpay, invest)
        msg = bot.send_message(message.chat.id, f'Категорія ⬇️', reply_markup=keyboard)
        bot.register_next_step_handler(msg, category_sum)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Сталася Помилка-1')


def category_sum(message):

    try:
        logging.info("Initialization command contact")
        chat_id = message.chat.id
        category = message.text
        finta = finta_dict[chat_id]
        parse_category = h.category_parser(category)
        finta.category = parse_category
        finta.category_abstraction = category

        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, f"Правильно: {finta.suma} грн, витрачено на {finta.category_abstraction}?",
                         reply_markup=markup)

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes = types.KeyboardButton(text="✅Вірно")
        cancel = types.KeyboardButton(text="⛔️Відміна")
        keyboard.add(yes, cancel)
        msg = bot.send_message(message.chat.id, f'Підтвердження ⬇️', reply_markup=keyboard)
        bot.register_next_step_handler(msg, final_step)
    except Exception as e:
        print(e)
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.reply_to(message, 'Сталася Помилка-2 Спробуйте ще раз)', reply_markup=markup)


def final_step(message):

    try:
        logging.info("Initialization command contact")
        chat_id = message.chat.id
        answer = message.text
        finta = finta_dict[chat_id]
        parse_answer = h.answer_parser(answer)
        finta.approved = parse_answer

        markup = types.ReplyKeyboardRemove(selective=False)
        if finta.approved:
            logging.info("Initialization command contact")
            time = datetime.now()
            bot.send_message(message.chat.id, f"✅Сума добавлена!\n"
                                              f"{finta.category_abstraction}: + {finta.suma} грн\n"

                                              f"Як буде потрібно просто додайте суму",
                             reply_markup=markup)
            db.protect(f"{message.from_user.id}", f"{finta.category}", int(finta.suma), time)
        else:
            bot.send_message(message.chat.id, f"💸Почнемо з початку)\nвведіть суму яку потрібно записати⬇️",
                             reply_markup=markup)

    except Exception as e:
        print(e)
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.reply_to(message, 'Сталася Помилка-3', reply_markup=markup)


@bot.message_handler(commands=['analitics'])
def analitics(message):
    try:
        logging.info("Initialization command contact")
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes = types.KeyboardButton(text="📊Загальна")
        cancel = types.KeyboardButton(text="📈Окремої категорії")
        keyboard.add(yes, cancel)
        msg = bot.send_message(message.chat.id, f'Вас цікавить аналітика по усім категоріям чи тільки окремої?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, analitics_all)
    except Exception as e:
            print(e)
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.reply_to(message, 'Сталася Помилка-4', reply_markup=markup)

def analitics_all(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == f"📊Загальна":
            analitica = db.info_all_category(f"{message.from_user.id}")
            bot.send_message(message.chat.id, f"{analitica}", reply_markup=markup)

        elif message.text == f"📈Окремої категорії":

            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Подключаем клавиатуру
            food = types.KeyboardButton(text="🍏продукти")
            utilities = types.KeyboardButton(text="🏠комунальні")
            cafe = types.KeyboardButton(text="☕️кафе")
            credit = types.KeyboardButton(text="💳кредити")
            dpay = types.KeyboardButton(text="💰+витрати")
            invest = types.KeyboardButton(text="📊інвестиції")

            keyboard.add(food, utilities, cafe, credit, dpay, invest)
            msg = bot.send_message(message.chat.id, f'Оберіть категорію ⬇️', reply_markup=keyboard)
            bot.register_next_step_handler(msg, analitics_category_final)

    except Exception as e:
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, f"💸Сталася Помилка-5', почнемо з початку)⬇️", reply_markup=markup)


def analitics_category_final(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    try:
        category = message.text
        parse_category = h.category_parser(category)
        analitica = db.info_one_category(f"{message.from_user.id}",f"{parse_category}",f"{category}")
        bot.send_message(message.chat.id, f"{analitica}",reply_markup=markup)

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"💸Сталася Помилка-6', почнемо з початку)⬇️", reply_markup=markup)


@bot.message_handler(commands=['delete'])
def dellete(message):
    try:
        logging.info("Initialization command contact")
        keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        all_dell = types.KeyboardButton(text="🔫Видалити усі витрати")
        last_dell = types.KeyboardButton(text="⚔️Видалити витрати категорії")
        keyboard.add(all_dell, last_dell)
        msg = bot.send_message(message.chat.id, f'Якщо вам потрібно видалити всі записи з усіх категорій то обирайте: 🔫Видалити усі витрати\n\n'
                                                f'А якщо вам треба видалити витрати певної категорії або останню суму в ній то: \n⚔️Видалити витрати категорії\n\n'
                                                f'🤔Що будемо видаляти?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dell_a)
    except Exception as e:
            print(e)
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.reply_to(message, 'Сталася Помилка-8.1 (dellete)', reply_markup=markup)

def dell_a(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == f"🔫Видалити усі витрати":
            logging.info("Initialization command contact")
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            yes = types.KeyboardButton(text="✅Так")
            cancel = types.KeyboardButton(text="⛔️Ні")
            keyboard.add(yes, cancel)
            msg = bot.send_message(message.chat.id,
                                   f'🔴Усі записи витрат будуть видалені, потім назад вже нічого не повернути'
                                   f'\n Ви впевнені ?🤔', reply_markup=keyboard)
            bot.register_next_step_handler(msg, dellete_all)

        elif message.text == f"⚔️Видалити витрати категорії":
            chat_id = message.chat.id
            suma = message.text
            finta = Finta(suma)
            finta_dict[chat_id] = finta

            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Подключаем клавиатуру
            food = types.KeyboardButton(text="🍏продукти")
            utilities = types.KeyboardButton(text="🏠комунальні")
            cafe = types.KeyboardButton(text="☕️кафе")
            credit = types.KeyboardButton(text="💳кредити")
            dpay = types.KeyboardButton(text="💰+витрати")
            invest = types.KeyboardButton(text="📊інвестиції")

            keyboard.add(food, utilities, cafe, credit, dpay, invest)
            msg = bot.send_message(message.chat.id, f'Оберіть категорію ⬇️', reply_markup=keyboard)
            bot.register_next_step_handler(msg, dell_category_final)
    except Exception as e:
            markup = types.ReplyKeyboardRemove(selective=False)
            print(e)
            bot.send_message(message.chat.id, f"💸Сталася Помилка-9', почнемо з початку)⬇️", reply_markup=markup)


def dellete_all(message):

        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == "✅Так":
            bot.send_message(message.chat.id, f"Всі дані назавжди видалені💸", reply_markup=markup)
            db.dell_id_all(f"{message.from_user.id}")

        elif message.text == "⛔️Ні":
            bot.send_message(message.chat.id, f"💸Правильний вибір🤝\n А тепре почнемо з початку)\nвведіть суму яку потрібно записати⬇️ \n або ви самі знаєте що робити", reply_markup=markup)

        else:
            bot.send_message(message.chat.id, f"💸Сталася Помилка-6 (dellete_all)', почнемо з початку)⬇️", reply_markup=markup)


def dell_category_final(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    try:
        chat_id = message.chat.id
        category = message.text
        finta = finta_dict[chat_id]
        parse_category = h.category_parser(category)
        finta.category = parse_category
        finta.category_abstraction = category

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        category_s = types.KeyboardButton(text="🧩Очистити категорію")
        category_row = types.KeyboardButton(text="📌Видалити останній запис")
        keyboard.add(category_s, category_row)
        msg=bot.send_message(message.chat.id,
                               f'🔴Видалення - процедура незворотна, враховуйте це при прийнятті рішення'
                               f'\n\n Оберіть наступний крок⬇️', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dell_category_final_o)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"💸Сталася Помилка-7 (dell_category_final)', почнемо з початку)⬇️",
                         reply_markup=markup)

def dell_category_final_o(message):

    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == "🧩Очистити категорію":
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            yes = types.KeyboardButton(text="✅Так")
            cancel = types.KeyboardButton(text="⛔️Ні")
            keyboard.add(yes, cancel)
            msg=bot.send_message(message.chat.id,
                               f'Ви впевнені🤔⬇️', reply_markup=keyboard)
            bot.register_next_step_handler(msg, toodo_dell_category)

        elif message.text == "📌Видалити останній запис":
                markup = types.ReplyKeyboardRemove(selective=False)

                finta = finta_dict[message.from_user.id]
                veiw = db.dell_id_row_veiw(f"{message.from_user.id}", f"{finta.category}")

                keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                yes = types.KeyboardButton(text="✅Так")
                cancel = types.KeyboardButton(text="⛔️Ні")
                keyboard.add(yes, cancel)

                bot.send_message(message.chat.id,
                                 f"Остання сума яку ви добавили в категорію\n{finta.category_abstraction}\n= {veiw} UAH",
                                 reply_markup=markup)

                msg = bot.send_message(message.chat.id, f"Вадаляємо ?⬇️", reply_markup=keyboard)
                bot.register_next_step_handler(msg, dell_row_sum_category)
    except Exception as e:
            markup = types.ReplyKeyboardRemove(selective=False)
            print(e)
            bot.send_message(message.chat.id, f"💸Немає що видаляти🤔 Або Сталася Помилка-8 (dell_category_final)',почнемо з початку)⬇️", reply_markup=markup)

def toodo_dell_category(message):
    try:

        finta = finta_dict[message.from_user.id]

        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == "✅Так":

            bot.send_message(message.chat.id, f"Усі витрати з категорії {finta.category_abstraction} \nбули видаленні 💸",
                                   reply_markup=markup)
            db.dell_id_category(f"{message.from_user.id}", f"{finta.category}")

        elif message.text == "⛔️Ні":
            bot.send_message(message.chat.id, f"💸Правильний вибір🤝\n А тепре почнемо з початку)\nвведіть суму яку потрібно записати⬇️ \n або ви самі знаєте що робити", reply_markup=markup)
    except Exception as e:
            print(e)
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, f"💸Сталася Помилка-9 (dell_category_final)', почнемо з початку)⬇️", reply_markup=markup)

def dell_row_sum_category(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == "✅Так":

            finta = finta_dict[message.from_user.id]
            bot.send_message(message.chat.id, f"🧹Витрата була видалена", reply_markup=markup)
            db.dell_id_row(f"{message.from_user.id}", f"{finta.category}")


        elif message.text == "⛔️Ні":
            bot.send_message(message.chat.id, f"А тепре почнемо з початку)\nвведіть суму яку потрібно записати⬇️ \nабо ви самі знаєте що робити", reply_markup=markup)

    except Exception as e:
            markup = types.ReplyKeyboardRemove(selective=False)
            print(e)
            bot.send_message(message.chat.id, f"💸Сталася Помилка-10' Або просто немає що видаляти), почнемо з початку)⬇️", reply_markup=markup)






@bot.message_handler(func=lambda message: True, content_types=["text"])
def message_from_user(message):
    user_id = message.from_user.id
    update_message_count(user_id)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200



if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))