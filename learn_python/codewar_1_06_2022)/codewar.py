"""
6-kyu
Bit Counting.
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

def count_bits(n):
    y = str(format(n, "b"))
    return y.count("1")

"""
6-kyu
Split Strings.
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
def solution(s):
    if len(s) % 2 != 0:
        s += "_"

    chunks = [s[i:i + 2] for i in range(0, len(s), 2)]
    return chunks


"""
7-kyu
Square Every Digit.
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
"""

def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))

"""
7-kyu
Binary Addition
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""
def add_binary(a,b):
    return f"{str(bin(a+b)[2:])}"


"""
7-kyu
Regex validate PIN code.
DESCRIPTION:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

import re
def validate_pin(pin):
    return bool(re.fullmatch("\d{4}|\d{6}", pin))

"""
7 kyu
Ones and Zeros.
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
"""
def binary_array_to_number(arr):
    return int(''.join([str(i) for i in arr]), 2)


"""
8 kyu
Returning Strings.
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
[Make sure you type the exact thing I wrote or the program may not execute properly]
"""
def greet(name):
    return f"Hello, {name} how are you doing today?"

"""
8 kyu
Sum of positive.
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.
"""
def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number
    return sum

"""
6 kyu
Does my number look big in this?
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcisstic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
"""
def narcissistic( value ):
    your_numbers = str(value)
    power = len(your_numbers)
    your_sum = 0
    for number in your_numbers:
        your_sum += pow(int(number), power)
    if your_sum == value:
        return True
    return False

"""
6 kyu
Which are in?
Given two arrays of strings a1 and a2 return a sorted array r in 
lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: r must be without duplicates.
"""
def in_array(array1, array2):
    result = []
    for item in array1:
        for item2 in array2:
            if item in item2 and item not in result:
                result.append(item)
                continue
    result.sort()
    return result


"""
6-kyu
Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2
The next number in having this property is 135.
See this property again: 135 = 1^1 + 3^2 + 5^3
We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:
sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.
sum_dig_pow(90, 100) == []
"""


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    res = []
    for num in range(a, b + 1):
        summed = sum(int(d) ** (idx + 1) for idx, d in enumerate(str(num)))
        if summed == num:
            res.append(num)
    return res

"""
6 kyu
Find the missing letter.
#Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)
Have fun coding it and please don't forget to vote and rank this kata! :-)
I have also created other katas. Take a look if you enjoyed this kata!
"""

def find_missing_letter(chars):
    missingChar = ''
    for i in range(0,len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            missingChar = chr(ord(chars[i])+1)

    return missingChar
