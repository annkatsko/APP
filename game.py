<<<<<<< HEAD
import random

kompukter = random.randint(1, 100)
attempt = 6
print(kompukter)
for i in range(attempt):
    a = input()
    if a == str(kompukter):
        print('Угадал!')
        break
    elif not a.isnumeric():
        print('Компуктер загадал число. Подсказка: Введи число!')
    elif int(a) > kompukter:
        print('Подсказка:Загаданое число меньше!')
    elif int(a) < kompukter:
        print('Подсказка: Загаданое число больше!')
if a == str(kompukter):
    print('Игра окончена!')
else:
=======
import random

kompukter = random.randint(1, 100)
attempt = 6
print(kompukter)
for i in range(attempt):
    a = input()
    if a == str(kompukter):
        print('Угадал!')
        break
    elif not a.isnumeric():
        print('Компуктер загадал число. Подсказка: Введи число!')
    elif int(a) > kompukter:
        print('Подсказка:Загаданое число меньше!')
    elif int(a) < kompukter:
        print('Подсказка: Загаданое число больше!')
if a == str(kompukter):
    print('Игра окончена!')
else:
>>>>>>> 6a8f7fda44b384ee4dba20cfb2498ce504d601aa
    print('Попытки кончились!')  