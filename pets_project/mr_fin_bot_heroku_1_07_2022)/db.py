import psycopg2
from config import *

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()

def inspect(id:int):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        return True
    else:
        return False

def add_db(id:int, username):
    print(f"🔴",id,username)
    db_object.execute("INSERT INTO users(id_telegram, username, phone) VALUES (%s, %s, %s);", (id, username, 213))
    db_connection.commit()
    return f"все окей"


def phone(id:int,phone:str):
    db_object.execute("UPDATE users SET phone = %s WHERE id_telegram = %s", (phone, id))
    db_connection.commit()
    return db_object.fetchone()

def protect(id, category_id, value, time):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        db_object.execute("INSERT INTO finance(user_id, category_id, value, time) VALUES (%s, %s, %s, %s)",
                          (id_user, category_id, value, time))
        return db_connection.commit()
    else:
        return False

def info_all_category(id):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        id_user = id_user[-1]

        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user}")
        allcoin = db_object.fetchall()
        asdd = []
        for i in allcoin:
            asdd.append(i[0])

        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id =1")
        food = db_object.fetchall()
        food_sum = []
        for i in food:
            food_sum.append(i[0])

        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id =2")
        utilities = db_object.fetchall()
        utilities_sum = []
        for i in utilities:
            utilities_sum.append(i[0])

        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id =3")
        cafe = db_object.fetchall()
        cafe_sum = []
        for i in cafe:
            cafe_sum.append(i[0])


        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id =4")
        credit = db_object.fetchall()
        credit_sum = []
        for i in credit:
            credit_sum.append(i[0])


        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id =5")
        dpay = db_object.fetchall()
        dpay_sum=[]
        for i in dpay:
            dpay_sum.append(i[0])


        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id =6")
        invest = db_object.fetchall()
        invest_sum =[]
        for i in invest:
            invest_sum.append(i[0])

        return  f"🍏продукти | {sum(food_sum)} UAH\n" \
                f"🏠комунальні | {sum(utilities_sum)} UAH\n" \
                f"☕️кафе | {sum(cafe_sum)} UAH\n" \
                f"💳кредити | {sum(credit_sum)} UAH\n" \
                f"💰+витрати | {sum(dpay_sum)} UAH\n" \
                f"📊інвестиції | {sum(invest_sum)} UAH\n\n" \
                f"💸Разом | {sum(asdd)} UAH"
    else:
        return False

def info_one_category(id,pars_category,category):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        id_user = id_user[-1]

        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user} AND category_id = {pars_category}")
        result = db_object.fetchall()
        sumcategory = []
        for i in result:
            sumcategory.append(i[0])
        return f"Загальна сума витрат категорії {category} \n= {sum(sumcategory)} UAH"

    else:
        return False


def dell_id_all(id):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        db_object.execute("DELETE FROM finance WHERE user_id = (%s)", id_user)
        db_connection.commit()
        return db_object.fetchone()

def dell_id_row_veiw(id,category):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        db_object.execute(f"SELECT value FROM finance WHERE user_id = {id_user[0]} AND category_id = {category[0]} ORDER BY id DESC LIMIT 1")
        result = db_object.fetchone()
        return result[0]


def dell_id_category(id,category):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        answer = id_user[0]
        answers = category[0]
        db_object.execute("DELETE FROM finance WHERE category_id = (%s) AND user_id = (%s)", (answers, answer))
        db_connection.commit()
        return f"🟢 фініш dell_id_category"

def dell_id_row(id,category):
    db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
    if db_object.fetchone():
        db_object.execute(f"SELECT id FROM users WHERE id_telegram = {id}")
        id_user = db_object.fetchone()
        db_object.execute(f"SELECT id FROM finance WHERE user_id = {id_user[0]} AND category_id = {category[0]} ORDER BY id DESC LIMIT 1")
        id_result = db_object.fetchone()

        db_object.execute("DELETE FROM finance WHERE id = (%s)", id_result)
        db_connection.commit()
        return f"🧹Витрата була видалена"