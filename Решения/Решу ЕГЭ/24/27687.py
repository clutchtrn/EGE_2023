f = open('files/27687.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] == 'Y':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('Y' * 10))
print(stroka.count('Y' * 11))
