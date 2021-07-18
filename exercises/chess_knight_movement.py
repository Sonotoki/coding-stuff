from itertools import product
# Решение задачи "Ход коня"
inputs = []

try_again = '\nВведите еще раз (Или Ctrl + C для выхода из программы).'
error_msg = 'Введенны недопустимые данные.' + try_again
wrong_args = 'Введены недопустимые значении (x и y должны быть меньше чем 8 и больше чем 0).' + try_again

splitter = ''.ljust(40, '-')
print(splitter + '\n Программа для определение "Ход коня" \n' + splitter)

while True:
    inputs = input('x1, y1, x2, y2 (ввести через пробел): ')
    inputs = list(map(int, inputs.split(' ')))
    try:
        if sum([True if x <= 8 and x >= 1 else False for x in inputs]) != 4:
            print(error_msg)
        else:
            x1, y1, x2, y2 = inputs
            del inputs  # is it really need to be done? Well, explicity is an important thing!
            break
    except:
        print(error_msg)

vertical = [[x, y] for x, y in list(product([x1-1, x1+1], [y1-2, y1+2]))]
horizontal = [[x, y] for x, y in list(product([x1-2, x1+2], [y1-1, y1+1]))]
knight_moves = vertical + horizontal
available_moves = [
    [x, y] for x, y in knight_moves if (x >= 1 and x <= 8) and (y >= 1 and y <= 8)
]
if [x2, y2] in available_moves:
    print('YES')
else:
    print('NO')
print("Всевозможные ходы: ", available_moves)
