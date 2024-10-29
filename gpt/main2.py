a = input("Введите числа через пробел: ")
b = list()
c = list()

for i in a.split():
    if i.isdigit():
        if int(i) % 2 == 0:
            b.append(int(i))
        else:
            c.append(int(i))

print(f"Чётные числа: {b}")
print(f"Нечётные числа: {c}")
