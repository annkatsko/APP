import random




def main():
    game = True
    while game:
        count_attempt = 1
        attempt = 5
        computer = random.randint(1, 100)
        user_number = input('Компьютер загадал число. Введите свое число! Чтобы получить подсказку дипазона чисел введите "?"')
        game_round = True
        while game_round:
            while not user_number.isnumeric() and not user_number == '?':
                print('Вы ввели букву или символ. Введите число!')
                user_number = input()
            if user_number == '?':
                print('Диапазон чисел от ' + str(computer - 10) + ' до ' + str(computer + 10) + ' У вас осталось попыток: ' + str(attempt+1 - count_attempt)) if computer > 10 else print('Диапазон чисел от ' + 1 + ' до ' + str(computer + 10) + ' У вас осталось попыток: ' + str(attempt+1 - count_attempt))
                continue
            if user_number == computer:
                print('Вы угадали!')
                game_round = False
                break
            check_answer()
            if count_attempt == attempt:
                print('Правильный ответ:' + str(computer))
                game_round = False
                break
            count_attempt += 1
        new_game()


def new_game():
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


def left_attempt():
    print('У Вас осталось попыток:' + str(attempt - count_attempt))


def check_answer():
    pass
    #if user_number > computer:
      #  print('Загаданое компьютером число меньше Вашего числа!')
      #  left_attempt()
    #else:
        #print('Загаданое компьютером число больше Вашего числа!')
        #left_attempt()


main()