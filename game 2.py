import random

kompukter = random.randint(1, 100)
attempt = 3
count_attempt = 1
print(kompukter)
user_number = input('Компуктер загадал число. Введите свое число!')
user_answer = None
game = True
while game:
    while count_attempt < attempt:
        if not user_number.isnumeric():
            print('Вы ввели букву или символ. Введите Число!')
            user_number = input()
        else:
            count_attempt += 1
            if user_number == str(kompukter):
                print('Вы угадали!')
                break
            elif user_number > str(kompukter):
                print('Загаданое компуктером число меньше Вашего числа!')
                print('У Вас осталось попыток:' + str(attempt+1 - count_attempt))
            elif user_number < str(kompukter):
                print('Загаданое компуктером число больше Вашего числа!')
                print('у Вас осталось попыток:' + str(attempt+1 - count_attempt))
            user_number = input()
    if count_attempt == attempt:
            user_answer = input('У вас кончились попытки :( Вы так и не угадали. Хотите сыграть еще раз? (Да/Нет)').lower()
            if user_answer == 'нет':
                print('Вы вышли из игры')
                game = False
            elif user_answer == 'да':
                kompukter = random.randint(1, 100)
                count_attempt = 1
                user_number = input('Играем снова! Компуктер загадал число. Введите свое число!')
                continue
    else:
        user_answer = input('Хотите сыграть еще раз? (Да/Нет)').lower()
        if user_answer == 'нет':
            print('Вы вышли из игры')
            game = False
        elif user_answer == 'да':
            kompukter = random.randint(1, 100)
            count_attempt = 1
            user_number = input('Играем снова! Компуктер загадал число. Введите свое число!')
            continue
