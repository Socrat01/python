

'''
task-1
Напишите функцию которая будет переводить возраст с Земного на Марсианский.
В году на Земле 365 дней а на марсе 687
def mars_age(age: int) -> int:
    pass
assert mars_age(10) == 5
assert mars_age(63) == 33
assert mars_age(1000) == 531
'''
mars_year = 687
earth_year = 365


def mars_age(*args: int):
    earth_days = int(*args) * 365
    mars_yers = earth_days // 687
    print(mars_yers)
    return mars_yers

try: #Попробывал как оно должно быть но еще нужно разобраться
    mars_year // earth_year
except Exception as e:
    print("Error", e)

mars_age(14)



"""
task-2
Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
 Если слово не передано то считать его "-" и возвращающую строку вида "[Имя] ты сегодня [слово]!"
# todo: ваш код функции
assert greet("111", "2") == "111 ты сегодня 2!"
assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
assert greet("николай") == "Николай ты сегодня -!"
"""
def greet(name,word="-"):
        return print(str(name),"ты сегодня", str(word))

greet("Andriy")


"""
task-3
Напишите функцию joinA которая принимает неограниченное количество значений
любого типа и возвращает строку где эти значения склеены через символ A
Попробуйте написать с помощью компрехеншена одной строкой return ___magic___
# todo: ваш код тут
assert joinA("Привет", "мир", "!") == "ПриветAмирA!"
assert joinA("Привет", 1, 2, 3, True) == "ПриветA1A2A3ATrue"
assert joinA() == ""
"""

def joinA(*args):
        return print("A".join([str(s) for s in args]))
joinA("asd", True, "sufgh")