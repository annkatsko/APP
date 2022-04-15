import random


game = True
round = True
while game:
    count_attempt = 1
    attempt = 5
    computer = random.randint(1, 100)
    while round:
        user_number = input('Компуктер загадал число. Введите свое число!')
        while not user_number.isnumeric():
            print('Вы ввели букву или символ. Введите Число!')
            user_number = input()
        if user_number == str(computer):
            print('Вы угадали!')
            raund = False
            break
        elif user_number > str(computer):
            print('Загаданое компуктером число меньше Вашего числа!')
            print('У Вас осталось попыток:' + str(attempt - count_attempt))
        else:
            print('Загаданое компуктером число больше Вашего числа!')
            print('У Вас осталось попыток:' + str(attempt - count_attempt))
        if count_attempt == attempt:
            round = False
            break
        count_attempt += 1
    while 1:
        user_answer = input('Хотите сыграть еще раз? (Да/Нет)').lower()
        if user_answer == 'нет':
            print('Вы вышли из игры')
            game = False
            break
        elif user_answer == 'да':
            break
        else:
            print('Kоманда не совсем понятна, повторите')