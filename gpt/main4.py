digits = input("Введите числа через пробел: ")

even_num = list()
odd_num = list()

for x in digits.split():
    try:
        i = int(x)
        if i % 2 == 0:
            even_num.append (i)
        else:
            odd_num.append (i)
    except ValueError:
        print(f"'{x}' не является корректным числом.")

print(f"Чётные числа: {even_num}")
print(f"Количество чётных чисел: {len(even_num)}")
print(f"Сумма чётных чисел: {sum(even_num)}")
print(f"Среднее значение чётных чисел: {round(sum(even_num)/len(even_num), 2)}")

print(f"Нечётные числа: {odd_num}")
print(f"Количество нечётных чисел: {len(odd_num)}")
print(f"Сумма нечётных чисел: {sum(odd_num)}")
print(f"Среднее значение нечётных чисел: {round(sum(odd_num)/len(odd_num), 2)}")

if (len(odd_num) + len(even_num)) % 2 != 0:
    odd_num[-1] += 1
    print(f"Измененный список нечётных чисел: {odd_num}")
