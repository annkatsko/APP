from itertools import count
import random

kompukter = random.randint(1, 100)
attempt = 6
count_attempt = 0
print(kompukter)
print('Введите число')
a = input()
while count_attempt < attempt:
    if not a.isnumeric():
        print('Компуктер загадал число! Введите Число!')
        a = input()
    else:
        count_attempt+=1
        if a == str(kompukter):
            print('Угадал!')
            break
        elif a > str(kompukter):
            print('Загаданое число больше!')
        elif a < str(kompukter):
            print('Загаданое число меньше!')
        a = input()
if count_attempt == attempt:
    print("Попытки кончились")
else:
    print('Игра окончена!')