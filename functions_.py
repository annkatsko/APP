from tokenize import Number


def main(number):
    f = {0: 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
    6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
    return f.get(number,'there is no such value')


print(main(0))