import random


game = True
raund = True
count_attempt = 1
while game:
    attempt = 3
    kompukter = random.randint(1, 100)
    print(kompukter)
    raund = True
    while raund:
        user_number = input('Компуктер загадал число. Введите свое число!')
        while not user_number.isnumeric():
            print('Вы ввели букву или символ. Введите Число!')
            user_number = input()
        if user_number == str(kompukter):
            print('Вы угадали!')
            raund = False
        elif user_number > str(kompukter):
            print('Загаданое компуктером число меньше Вашего числа!')
            print('У Вас осталось попыток:' + str(attempt - count_attempt))
        else:
            print('Загаданое компуктером число больше Вашего числа!')
            print('у Вас осталось попыток:' + str(attempt - count_attempt))
        if count_attempt == attempt:
            raund = False
        count_attempt +=1
    user_answer = input('Хотите сыграть еще раз? (Да/Нет)').lower()
    if user_answer == 'нет':
        print('Вы вышли из игры')
        game = False
    elif user_answer == 'да':
        raund = True