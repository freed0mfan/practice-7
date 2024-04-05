N_K_R = input('N_K_R: ')
N = int(N_K_R.split(' ')[0])
K = int(N_K_R.split(' ')[1])
R = int(N_K_R.split(' ')[2])

day = 1
length = N
while length < R:
    length *= (1 + 0.01 * K)
    day += 1

print(day)
