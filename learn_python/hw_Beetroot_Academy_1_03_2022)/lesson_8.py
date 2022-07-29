
task-1
def favourite_movie():
    your_m = str(input("Whrite your favourite movie: "))
    print("Мой любимый фильм назван: ", your_m)
favourite_movie()

task-2
def make_country(name, capital):
    country = {name:capital}
    for x in country.keys():
        print(x, country[x])

make_country("Ukraine", "Khmelnitskyi")
make_country("Ukraine", "Rivne")
make_country("Ukraine", "Kyiv")


task-3
def make_operation(operator, *args):
    total = args[0]
    for i in args[1:]:
        if operator == "+":
            total += i
        elif operator == "-":
            total -= i
        elif operator == "*":
            total *= i
        else:
            print("Not corect operation")
    print(total)

make_operation("+", 7, 7, 2, 23)
make_operation("-", 5, 5, -10, -20)
make_operation("*", 7, 6, 12)