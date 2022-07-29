Task 1
class Person():

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Здраствуйте, меня зовут {self.name} {self.lastname} и мне {self.age} лет")

a = Person("Алекс", "Стешковский", 75)
b = Person("Стас", "Цепиш", 96)
c = Person("Олег", "Цапко", 36)
a.talk()
b.talk()
c.talk()

Task 2

class Dog():
    def __init__(self, age):
        self.age = age

    def human_age(self):
        age_factor = 7
        sum = self.age // age_factor
        print(sum)

a = Dog(208)
a.human_age()


task-3

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController():
    def __init__(self,channels):
        self.channels = channels
        self.n_channels = self.channels[0]

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, number):
        self.n_channels = self.channels[number-1]
        return self.n_channels

    def next_channel(self):
        if self.channels.index(self.n_channels)==len(self.channels)-1:
            self.n_channels = self.channels[0]
            return self.n_channels
        else:
            self.n_channels = self.channels[self.channels.index(self.n_channels)+1]
            return self.n_channels

    def previous_channel(self):
        if self.channels.index(self.n_channels) == 0:
             return f"{self.n_channels} = {self.channels[-1]}"
        else:
            return f"{self.channels[self.channels.index(self.n_channels)-1]}"

    def current_channel(self):
        return self.channels[0]

    def s_exist(self, i):
        for number, name in enumerate(self.channels):
            if i == number + 1 or i == name:
                return True
        return False

controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.s_exist(4))
