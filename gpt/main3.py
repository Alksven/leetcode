digits = input("Введите числа через пробел: ")

positive_num = list()
negative_num = list()
even_num = list()
odd_num = list()

for x in digits.split():
    try:
        i = int(x)
        if i % 2 == 0:
            even_num.append (i)
        else:
            odd_num.append (i)
        if i >= 0:
            positive_num.append (i)
        else:
            negative_num.append (i)
    except ValueError:
        print(f"'{x}' не является корректным числом.")

print(f"Чётные числа: {even_num}")
print(f"Нечётные числа: {odd_num}")
print(f"Положительные числа: {positive_num}")
print(f"Отрицательные числа: {negative_num}")
print(f"Сумма чётных чисел: {sum(even_num)}")
print(f"Сумма нечётных чисел: {sum(odd_num)}")
print(f"Сумма положительных чисел: {sum(positive_num)}")
print(f"Сумма отрицательных чисел: {sum(negative_num)}")



