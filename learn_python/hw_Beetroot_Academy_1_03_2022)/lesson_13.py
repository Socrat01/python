


# task-1

class Animal:
   def __init__(self, name):
       self.name = name


class Cat(Animal):

    def talk(self):
        return f"Кошка {self.name} говорит: мяю"

class Dog(Animal):

    def talk(self):
        return f"Собака {self.name} говорит: гав-гав"

c = Cat("Васько")
d = Dog("Жмурко")
print(c.talk())
print(d.talk())
print(c.name)
print(d.name)


# task-3
class Fraction():

    def test(n: str, a: int, b: int) -> (float, str):
        return {
        "+": a+b,
        "-": a-b,
        "*": a*b,
        "/": a/b
               }[n], n

a = Fraction
print(a.test("+", 2.23, 3.23))
print(a.test("*", 2.23, 3.23))
print(a.test("-", 2.23, 3.23))
print(a.test("/", 2.23, 3.23))