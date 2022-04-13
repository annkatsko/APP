import random

kompukter = random.randint(1, 100)
attempt = 3
count_attempt = 1
print(kompukter)
print('Компуктер загадал число. Введите свое число!')
a = input()
again = None
while True:
    while count_attempt < attempt:
        if not a.isnumeric():
            print('Вы ввели букву или символ. Введите Число!')
            a = input()
        else:
            count_attempt+=1
            if a == str(kompukter):
                print('Вы угадали!')
                break
            elif a > str(kompukter):
                print('Загаданое компуктером число меньше Вашего числа!')
                print('У Вас осталось попыток:' + str(attempt+1 - count_attempt))
            elif a < str(kompukter):
                print('Загаданое компуктером число больше Вашего числа!')
                print('у Вас осталось попыток:' + str(attempt+1 - count_attempt))
            a = input()
    if count_attempt == attempt:
        print('У вас кончились попытки :( Вы так и не угадали. Хотите сыграть еще раз? (Да/Нет)')
        again = input().lower()
    else:
        print('Игра окончена! Хотите сыграть еще раз? (Да/Нет)')
        again = input().lower()
    if again == 'да':
        True
    else:
        False
