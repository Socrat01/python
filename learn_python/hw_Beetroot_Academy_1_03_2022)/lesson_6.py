'''
task-1
'''
answ = input("Write word: ")
if len(answ) >= 2:
	result = answ[:2] + answ[-2:]
	print(f"{result}")
else:
	print("Nooo")



'''
task-2
'''

number = int(input("enter the number: "))
number_2string = str(number)
if len(number_2string) == 9:
	print("Good")
else:
	print("Noo")



'''
task-3
'''

name = "serhii"
name_1 = input("Enter your name: ")
if name_1 == name.lower() or name_1 == name.upper() or name_1 == name.title():
	print("True")
else:
	print("Nooo")

'''другой вариант'''
name = "serhii"
name_1 = input("Enter your name: ").lower()
if name_1 == name:
	print("True")
else:
	print("Nooo")