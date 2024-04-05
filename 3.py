import math

n = int(input('Введите целое число: '))
while math.sqrt(n) % 1 != 0:
    print('Это неполный квадрат:(')
    n = int(input('Введите другое число: '))
else:
    print(f'Ура! {n} -  полный квадрат')
