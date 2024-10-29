# text = input("Введите фразу: ")
# text_a = ""
#
# for i in text:
#     if i.isalpha():
#         text_a += i.lower()
#
# text_b = text_a[::-1]
# if text_a == text_b:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")

text = input("Введите фразу: ")

ready_text = ''.join(i.lower() for i in text if i.isalnum())

if ready_text == ready_text[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром.")