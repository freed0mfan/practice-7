n = int(input('n: '))
d = n
moves = 1
while d >= 2:
    d /= 2
    moves += 1

print(moves)
