# lsn05 (Svyat33)

# Lesson-6

task-1
import random
l = []
i = 1
while i <= 10:
    l.append(random.randint(0,100))
    i += 1
print(l)
print("Max ", max(l))
print("Min ", min(l))

'''
Преобразование типов и слайсы.
Превратите полученную от пользователя строку в тапл.
Выведите строку содержащую только буквы на четных позициях.
'''
task-2
list = ["П", "р", "и", "в", 'і', "т"]
print("The original list : " + str(list))
list_a = []
list_b = []
for i in range(0, len(list)):
	if i % 2:
		list_a.append(list[i])
	else :
		list_b.append(list[i])
print(f"Chetnyi: {list_a}")
print(f"NEChetnyi: {list_b}")






