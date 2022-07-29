

"""
Create a class method named `validate`, which should be called from the `__init__`
method to validate parameter email, passed to the constructor. The logic inside the `validate`
method could be to check if the passed email parameter is a valid email string.
"""
# from _ctypes_test import func
# from typing import Optional
#
# class Valid_emeil:
#     def __init__(self, address):
#         self.address = address
#         self.validate()
#
#     def validate(self):
#         import re
#         valid_email = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
#         if not re.search(valid_email, self.address):
#             return False
#         else:
#             return True
#
# address0 = "sdasdasdom@gmailom"
# address = "asaa@gmail.com"
# print(Valid_emeil(address0).validate())
# print(Valid_emeil(address).validate())



"""
Реализуйте 2 класса, первый — Босс, а второй — Рабочий.
У Worker есть свойство «boss», и его значение должно быть экземпляром Boss.
Вы можете переназначить это значение, но вы должны проверить, является ли новое значение Boss.
У каждого Босса есть список своих рабочих.
 
Вы должны реализовать метод, позволяющий добавлять рабочих к Boss.
Вам не разрешено добавлять экземпляры класса Boss в список рабочих напрямую через доступ к атрибуту,
вместо этого используйте геттеры и сеттеры!

Вы можете реорганизовать существующий код.
id_ - это просто случайное уникальное целое число

"""

# class Person:
#
#     def __init__(self, id_: int, name: str, company: str = ""):
#         self.id_ = id_
#         self.name = name
#         self.company = company
#
# class Boss(Person):
#
#     def __init__(self, id_: int, name: str, company: str):
#         super().__init__(id_, name, company)
#         self.workers = []
#
#     @property
#     def workers_upend(self):
#         return self.workers
#
#     @workers_upend.setter
#     def workers_upend(self, value):
#         if type(value) == Worker:
#             value.boss = self
#             value.company = self.company
#             self.workers.append(value)
#
#     def __repr__(self):
#         workers_string = '\n'.join([i.name for i in self.workers])
#         return f"Босса зовут: {self.name} | Название компании: {self.company} | Работники: {workers_string}"
#
# class Worker(Person):
#
#     def __init__(self, id_: int, name: str, company: str='', boss: Optional[Boss]=None):
#         super().__init__(id_, name, company)
#         self.boss = boss
#
#     def __repr__(self):
#         return f"Имя работника: {self.name} |  Название компании: {self.company} | Босс: {self.boss.name}"
#
# def main():
#     c = Boss(id_=12, name="Alex", company="Inter")
#     a = Boss(id_=11, name="Serhii", company="Plus")
#     w = Worker(id_=21, name="Oleg")
#     d = Worker(id_=22, name="Igant")
#     x = Worker(id_=55, name="Slava")
#     z = Worker(id_=15, name="Max")
#     c.workers_upend = w
#     c.workers_upend = d
#     a.workers_upend = x
#     a.workers_upend = z
#
#
#     print(c)
#     print("======")
#     print(a)
#     print("======")
#     for i in c.workers_upend:
#         print(i)
#     for i in a.workers_upend:
#         print(i)
#
# if __name__ == '__main__':
#     main()

#task-3
"""Напишите класс TypeDecorators, который имеет несколько методов для
преобразования результатов функций в заданный тип (если это возможно):

methods:
to_int
to_str
to_bool
to_float

Don't forget to use @wraps

```"""

from functools import wraps

class TypeDecorators:

    def to_int(self):

        def decorator_inner(func):
            @wraps(func)
            def wrapper(*args):
                return int(func(*args))
            return wrapper
        return decorator_inner


    def to_str(self):
        def decorator_inner(func):
            @wraps(func)
            def wrapper(*args):
                return str(func(*args))
            return wrapper
        return decorator_inner

    def to_float(self):
        def decorator_inner(func):
            @wraps(func)
            def wrapper(*args):
                return float(func(*args))
            return wrapper
        return decorator_inner

    def to_bool(self):
        def decorator_inner(func):
            @wraps(func)
            def wrapper(*args):
                return bool(func(*args))
            return wrapper
        return decorator_inner


@TypeDecorators.to_int
def do_something(string: str):
    return string

@TypeDecorators.to_bool
def do_nothing(string: str):
    return string

print(do_something(20))
print(do_nothing("30"))
print(do_nothing(True))
print(do_something(False))
