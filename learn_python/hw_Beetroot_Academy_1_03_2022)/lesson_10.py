task-1

def new_file():
    with open("myfile.txt", "w") as file:
        file.write("Hello file world!\n")

def file_reader():
    with open("myfile.txt", "r") as file:
        return file.read()

new_file()
alex = file_reader()
print(alex)




task-2
import json
from pathlib import Path
import time

path_to_file = 'phonebook.json'
path = Path(path_to_file)

if not path.is_file():
    phonebook = []
    with open("phonebook.json", "w") as jsonfile:
        json.dump(phonebook, jsonfile)

def add_new_contact(first_name, last_name, phone_number, country, city):

    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f'{first_name} {last_name}',
        'phone_number': phone_number,
        'country': country,
        'city': city
    }
    with open('phonebook.json', 'r') as jsonfile_for_read:
        data = json.load(jsonfile_for_read)
        data.append(contact)

    with open('phonebook.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def search(criteria):

    with open('phonebook.json', 'r') as jsonfile_for_read:
        data = json.load(jsonfile_for_read)

    for i in data:
        if criteria in i['phone_number']:
            print(('-' * 24))
            print(f"Есть такой номер телефона как : {i['phone_number']}\nЭто номер телефона абонента   : {i['first_name']} {i['last_name']}")
            print(('-' * 24))

        elif criteria in i['first_name']:
            print(('-' * 24))
            print(f"Есть такой абонент как : {i['first_name']} {i['last_name']}\nНомер телефона абонента : {i['phone_number']}")
            print(('-' * 24))

        elif criteria in i['last_name']:
            print(('-' * 24))
            print(f"Есть такой абонент как : {i['last_name']} {i['first_name']} \nНомер телефона абонента : {i['phone_number']}")
            print(('-' * 24))

        elif criteria in i['full_name']:
            print(('-' * 24))
            print(f"Есть такой абонент как : {i['full_name']}\nНомер телефона абонента: {i['phone_number']}")
            print(('-' * 24))

        elif criteria in i['country']:
            print(('-' * 24))
            print(f"Есть такой абонент из страны : {i['country']}\nФИО абонента : {i['full_name']}\nНомер телефона абонента: {i['phone_number']}")
            print(('-' * 24))

        elif criteria in i['city']:
            print(('-' * 24))
            print(f"Есть такой абонент из города: {i['city']}\nФИО абонента : {i['last_name']} {i['first_name']}\nНомер телефона абонента : {i['phone_number']}")
            print(('-' * 24))
        else:
            print(('-' * 24))
            print("Нету абонента с такими данными :(")
            print(('-' * 24))

def delete_contact(number):

    with open('phonebook.json', 'r') as jsonfile_for_read:
        data = json.load(jsonfile_for_read)

    for i in data:
        if number in i['phone_number']:
            data.pop(data.index(i))
            print("номер был удален")
        else:
            print("номер не найден")
    with open('phonebook.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def update():

    with open('phonebook.json', 'r') as jsonfile_for_read:
        data = json.load(jsonfile_for_read)

    num = input("ввидете номер который хотите обновить: ")
    new_num = input("ввидете новый номер для этого контакта: ")

    for i in data:
        if num in i['phone_number']:
            i['phone number'] = new_num
            print("контакт обновлен")
        else:
            print("контакт не найден")

    with open('phonebook.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def all():
    with open('phonebook.json', 'r') as jsonfile_for_read:
        data = json.load(jsonfile_for_read)
        for i in data:
            print(i)

def menu():
    time.sleep(1)
    print("-" * 24)
    print("*" * 24)
    print("показать тел.книгу ----- all")
    print("создать новый контакт -- add")
    print("удалить контакт -------- del")
    print("поиск по тел.книге ----- srh")
    print("обновить контакт ------- upd")
    print("выйти с програмы ------- xxx")

    print("*" * 24)
    print("-" * 24)

while True:
    menu()
    command = input("Ожидаю команды:\n")
    if command == "menu":
        menu()
    elif command == "add":
        first_name = input("Напишите имя: ")
        last_name = input("Напишите фамилию: ")
        full_name = f"{first_name} {last_name}"
        phone_number = input("Напишите номер телефона: ")
        country = input("С какой вы страны: ")
        city = input("Ваш город: ")
        time.sleep(1)
        print("Супер, контакт создан")
        add_new_contact(first_name, last_name, phone_number, country, city)

    elif command == "del":
        number = input("Ввидите номер для удаления: ")
        delete_contact(number)
    elif command == "srh":
        criteria = input("Ввидите имя, страну, или номер для поиска: ")
        search(criteria)
    elif command == "upd":
        update()
    elif command == "all":
        all()
    elif command == "xxx":
        break
