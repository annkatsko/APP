import random
game = True
while game:
    kompukter = random.randint(1, 100)
    attempt = 3
    count_attempt = 1
    print(kompukter)
    user_number = input('Компуктер загадал число. Введите свое число!')
    user_answer = None
    raund = True
    while raund:
        if count_attempt == attempt:
            raund = False
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
    user_answer = input('У вас кончились попытки :( Вы так и не угадали. Хотите сыграть еще раз? (Да/Нет)').lower()
    if user_answer == 'нет':
        print('Вы вышли из игры')
        game = False
    elif user_answer == 'да':
        continue
    else:
        user_answer = input('Хотите сыграть еще раз? (Да/Нет)').lower()
        if user_answer == 'нет':
            print('Вы вышли из игры')
            game = False
        elif user_answer == 'да':
            continue