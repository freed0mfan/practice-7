ans = int(input('Ответ: '))
x = 1
while x <= ans:
    if ans == x:
        print('верно')
        break
    else:
        x += x
else:
    print('неверно')
