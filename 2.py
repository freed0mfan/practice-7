user = input()
for i in range(len(user)):
    if (i + 1) % 3 == 0:
        print(user[i], end='')
