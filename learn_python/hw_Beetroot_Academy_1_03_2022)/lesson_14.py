task-1
def local():
    a = 1
    b = 2
    sad = 213
    return local.__code__.co_nlocals

a = local()
print(a)

task-2
def make_function():
    return function()

def function():
    print("доброго вечора ми з України")

make_function()

task-3
def choose_func(nums: list, func1, func2):
    if all(i > 0 for i in nums):
        return func1(nums)
    else:
        return func2(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums2 = [1, -2, 3, -4, 5]
nums1 = [1, 2, 3, 4, 5]
choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)
print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
