import json
import logging



def read_json():
    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)
    return data


# додаємо контакт в БД
def add_db(from_user_id,phone):
    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)
    json_data = {"id": from_user_id,
                  "phone": phone,
                  "finance": { "food": [0] ,
                               "utilities": [0],
                               "cafe": [0],
                               "credit": [0],
                               "dpay": [0],
                               "invest": [0]
                               }}
    data.append(json_data)
    with open('db.json', 'w') as f:
        json.dump(data, f)
    # print(data)
    return data

# print(add_db("001221","067544"))

# перевіряємо чи є контакт в БД і якзо немає викликаємо функцію add_db()
def inspect(from_user_id,phone):

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)

        for i in data:
            print(i['id'])
        if from_user_id in i['id']:
            # print(i['id'])
            return f"✅Ви вже зареєстровані"
        elif from_user_id not in i['id']:
            add_db(from_user_id, phone)
            return f"⛔️Вас немає в базі, але :\n✅Тільки що реєстрація пройшла успішно"
        else:
            return f"⛔⛔⛔"
# print(inspect('00110',"06"))

# ми вибираємо id і додаємо в нього нові данні по витратам
def add_sum(from_user_id,category,add: int):


    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)
        # print(data)

        for i in data:
            print(i["id"])
            if from_user_id == i["id"]:
                i['finance'][category].append(add)
                with open('db.json', 'w') as f:
                    json.dump(data, f)
                break




def info_one_category(from_user_id,category,category_abstraction): # виводимо інформацію по витратам користувача по категоріям

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)

        for i in data:
            if from_user_id == i["id"]:
                return f"Загальна сума витрат категорії {category_abstraction} \n= {sum(i['finance'][category])} UAH"


# print(info_one_category('38847596',f"cafe","🍏продукти"))

def info_all_category(from_user_id): # виводимо інформацію по витратам користувача по категоріям

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)

        for i in data:
            if from_user_id == i["id"]:
                return f"🍏продукти | {sum(i['finance']['food'])} UAH\n" \
                       f"🏠комунальні | {sum(i['finance']['utilities'])} UAH\n" \
                       f"☕️кафе | {sum(i['finance']['cafe'])} UAH\n" \
                       f"💳кредити | {sum(i['finance']['credit'])} UAH\n" \
                       f"💰+витрати | {sum(i['finance']['dpay'])} UAH\n" \
                       f"📊інвестиції | {sum(i['finance']['invest'])} UAH\n\n" \
                       f"💸Разом | {(sum(i['finance']['food'])+(sum(i['finance']['utilities']))+(sum(i['finance']['cafe']))+(sum(i['finance']['credit']))+(sum(i['finance']['dpay']))+(sum(i['finance']['invest'])))} UAH" #,{sum(i['finance']['cafe'])},{sum(i['finance']['credit'])},{sum(i['finance']['dpay'])},sum(i['finance']['invest'])})}  uah\n" \

# print(info_all_category('2752566'))

def dell_id_row(from_user_id,category): # видаляємо останній запис в певній категории БД певного контакта

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)

        for i in data:

            if from_user_id == i["id"]:
                try:
                    print(i['finance'][category])
                    i['finance'][category].pop(-1)
                    print(i['finance'][category])

                    with open('db.json', 'w') as f:
                        json.dump(data, f)
                    break
                except Exception as e:
                    return f"Витрат немає - в категорія 0 витрат"



def dell_id_row_veiw(from_user_id,category): # видаляємо останній запис в певній категории БД певного контакта

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)

        for i in data:

            if from_user_id == i["id"]:
                try:
                    print(i['finance'][category])
                    # print(i['finance'][category].pop(-1))
                    return i['finance'][category].pop(-1)
                    # print(i['finance'][category])

                    # with open('db.json', 'w') as f:
                    #     json.dump(data, f)
                    # break
                except Exception as e:
                    return f"Витрат немає - в категорія 0 витрат"


# print(dell_id_row_veiw('38847596',f"food"))

def dell_category_row(from_user_id,category): # видаляємо витратити в одній з категорій

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)
        for i in data:
            if from_user_id == i["id"]:
                try:
                    del i['finance'][category][0:]

                    with open('db.json', 'w') as f:
                       json.dump(data, f)
                    break

                except Exception as e:
                    return f"⛔️Сталася помилка, спробуйте щераз"

# print(dell_category_row('38847596',f"food"))

def dell_id_all(from_user_id): # видаляємо витрати з усіх категорій але контакт залишаємо

    with open('db.json') as f:
        file_content = f.read()
        data = json.loads(file_content)
        for i in data:
            if from_user_id == i["id"]:
                try:
                    del i['finance']['food'][0:]
                    del i['finance']['utilities'][0:]
                    del i['finance']['cafe'][0:]
                    del i['finance']['credit'][0:]
                    del i['finance']['dpay'][0:]
                    del i['finance']['invest'][0:]

                    with open('db.json', 'w') as f:
                       json.dump(data, f)
                    break

                except Exception as e:
                    return f"⛔️Сталася помилка, спробуйте щераз"

#
# print(dell_id('38847596'))




