lsn01 (Svyat33)


task-1
total = 44
rezl = round(44*0.8)
print("Для успешного окончания курса надо сдать {} домашек".format(rezl))


task-2
x1, y1 = 10, 15
x2, y2 = 5, 8
distance = ((x2 - x1))**2 +(y2 - y1)**2**0.5)
print(f"відстань між точками = {round(distance, 1)}")

task-3
x, y, z = 30, 23, 8
sheet_price = 600
sheet_size = 3*4
need_size = (((x**2)+(y**2))**0.5 ) * z
need_sheets = need_size // sheet_size + 1
print(f"Необходимое количество: {int(need_sheets)} шт"
f"\n Сума: {int(need_sheets * sheet_price)} грн"
f"\n Залишок шиферу: {round(need_sheets * sheet_size % need_size), 2} m^2")


task-4
var1 = 'pyThoN'
var1 = var1.lower().capitalize()
assert var1 == 'Python'

var1 = var1.upper()
assert var1 == 'PYTHON'

var1 = var1.lower()
assert var1 == 'python'


var1 = " python "
var1 = var1.strip()
assert var1 == 'python'


task-5
name = "Остап"
print("Привет "+name)
print(f"Привет {name}!")
print("Привет {}".format(name))
print("Привет %s!" % name)


task-6
price = 12
weight = 3.4121
rezul = round((price * weight), 2)
rezul = f"Итого: {rezul}"
print(rezul)

task-7
number = 12
username = "ираклий"
access_mask = 54
hour_price = 15.321
rez = f"{str(number).zfill(6)} {username.capitalize()} {bin(access_mask) [2:]} {round(hour_price, 2)}"
print (rez)

task-8
base_str = 'Корова'
rez = base_str.replace("К", "В").replace("в", "н")
print(rez)


task-9
a = 10
b = 55
a, b, = b, a



