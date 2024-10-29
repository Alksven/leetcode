"""1 вариант"""

import math

# c = int(input("Введите число: "))
# b = math.factorial(c)
# print(f'Факториал {c} = {b}')

"""2 вариант"""
c = int(input("Введите число: "))
summ = 1
for i in range(1, c+1):
    summ *= i
print(summ)