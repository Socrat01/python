#task-1
"""
Создайте свою собственную реализацию встроенной функции enumerate
с именем with_index, которая принимает два параметра: iterable и start,
по умолчанию 0. Советы: см. документацию по функции enumerate.
"""
# import itertools
#
# def with_index(iterable, start=0):
#
#     for i in iterable:
#         yield start,i
#         start += 1
#
# w = [1,234234,324,"www",232]
# print(list(with_index(w,1)))

#task-2
"""
Создайте свою собственную реализацию встроенной функции range с именем in_range(),
которая принимает три параметра: `start`, `end` и необязательный шаг.
Советы: см. документацию по функции `range` 
"""
def in_range(start, end, step=1):

    if step > 0:
        while start < end:
            yield start
            start+=step

print(list(in_range(2, 6, 2)))

#task-3
"""
Создайте свою собственную реализацию итерации, которую можно использовать внутри цикла for-in.
Также добавьте логику для извлечения элементов с использованием синтаксиса квадратных скобок.

Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets synta
"""
class Iterbl:
    def __init__(self, iterabl):
        self.iterabl = iterabl
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.iterabl):
            raise StopIteration
        else:
            self.index+=1
            return self.iterabl[self.index-1]

    def __getitem__(self, item):
        return self.iterabl[item]

    def __len__(self):
        return len(self.iterabl)

itter=("One", "Two","Thre")
a = Iterbl(itter)
for i in a:
    print(i)
print()

for i in range(len(a)):
    print(a[i])

