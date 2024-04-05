temp = 37.4
counter = 0
while temp != 0:
    temp_previous = temp
    temp = float(input('Температура: '))
    if temp == 0:
        break
    elif temp < temp_previous:
        counter += 1

print(counter)
