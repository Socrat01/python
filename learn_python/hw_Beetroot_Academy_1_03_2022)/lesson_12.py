
task-1
class Person:
    def __init__(self, name, lastname, age=""):
        self.name = name
        self.lastname = lastname
        self.age = age

class Student(Person):
    def __init__(self, name, lastname, age="", curs=""):
        super().__init__(name, lastname, age)
        self.curs = curs

    def allinfo(self):
        return f"Студент: {self.name} {self.lastname}, Возраст: {self.age}, Курс: {self.curs}"

class Teacher(Person):
    def __init__(self, name, lastname, age="",price="", advance_one=""):
        super().__init__(name, lastname, age)
        self.price = price
        self.advance_one = advance_one

    def allinfo(self):
        return f"Учитель: {self.name} {self.lastname}, Возраст: {self.age}, Зарплата: {self.price}, Уровень знаний: {self.advance_one}"

a = Teacher(name="Наташа", lastname="Иванова",age="26", price="1000$", advance_one="Best Teacher")
b = Student(name="Сергей", lastname="Любчинко",age="18",curs="Фульдшер")
print(a.allinfo())
print(b.allinfo())


task-2
class Mathematician:
   def square_nums(self,n):
       return [i**2 for i in n]

   def remove_positives(self,n):
       return [i for i in n if i<0]

   def filter_leaps(self,n):
       return [i for i in n if i % 4 == 0]


print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))


task-3
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 0
        print(f'{self.type}, {self.name}, {self.price}')

class ProductStore():
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        self.products.append(product)
        product.amount = amount
        print("Продукт добавлен")
        # self.amount = amount
        #+30%

    def set_discount(self, identifier, percent):
        for i in self.products:
            if i.name == identifier or i.type == identifier:
                i.discount = percent
                i.price = i.price - (i.price*percent/100)
        print(f"Дисконд добавлен: {percent}")

    def sell_product(self, product_name, amount):
        for i in self.products:
            if i.name == product_name and i.amount >= amount:
                i.amount -= amount
                print("Продукт продан")

    def get_income(self):
        return len(self.products)


    def get_all_products(self):
        products = []
        for i in self.products:
            products.append(
                {
                    'type': i.type,
                    'name': i.name,
                    'price': i.price,
                    'amount': i.amount,
                    'discount': i.discount

                }
            )
        return [i for i in products]

    def get_product_info(self, product_name):
        for i in self.products:
            if i.name == product_name:
                return i.name, i.discount

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
print("==========")
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
s.sell_product('Football T-Shirt', 5)
print(s.get_product_info('Ramen'))
print(s.get_product_info('Football T-Shirt'))
print(s.get_income())
print(s.get_all_products())
print(s.set_discount(p2))

task-4
import datetime

class CustomException(Exception):
    def __init__(self, msg):
        self.massage = str(msg)
        self.time = datetime.datetime.now()

    def save(self):
        with open("Log.txt", "a") as file:
            file.write(f"You have error {self.massage} : in {self.time})\n")

a1 = CustomException(ValueError)
a1.save()

