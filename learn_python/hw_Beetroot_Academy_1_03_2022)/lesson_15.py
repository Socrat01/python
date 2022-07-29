
"""
# task-1
Напишите декоратор, который печатает функцию с переданными ей аргументами.
ПРИМЕЧАНИЕ! Он должен печатать функцию, а не результат ее выполнения!
"""
def logger(func):
    def alta(*args):
        return func(*args)
    return alta

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(22,21))
print(square_all(22,21))
"""
task-2
Напишите декоратор, который берет список стоп-слов и заменяет их * внутри декорированной функции.
"""
def stop_words(words: list):
    def n_decoration(func):
        def n1_decoration(name):
            funct1 = func(name)
            for i in words:
                funct1 = funct1.replace(i, "*")
            return funct1
        return n1_decoration
    return n_decoration

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan("Alex"))

"""
task-3
Напишите декоратор arg_rules, который проверяет аргументы, переданные функции.
Декоратор должен принимать 3 аргумента:
max_length: 15
type_: str
contains: [] - список символов, которые должен содержать аргумент
Если какая-то из проверок правил возвращает False,
функция должна вернуть False и вывести причину ошибки; в противном случае вернуть результат.
# """
def arg_rules(type_: type, max_length: int, contains: list):
        def arg_decoration(func):
            def arg_func(name):
                if type(name) == type_ and len(name) <= max_length:
                    for i in contains:
                        if i in name:
                            return func(name)
                if type(name) != type_:
                    return f"False in type: {name}"
                if len(name) >=max_length:
                    return f"False in len: {name}"
                else:
                    return f"False in contains {name}"
            return arg_func
        return arg_decoration


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
print(create_slogan("sd@"))
