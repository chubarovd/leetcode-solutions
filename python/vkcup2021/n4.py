n = int(input())

if n == 2:  # нет решения
    print(-1)
    exit()

result = [[]]
left = n

# выделим ближайший квадрат
a = int(n**(0.5))

# пробуем вырезать "центральный квадратный" кусок
if (n - a**2) % 2 != 0:
    # если остаток не поделится на два - фиг нам! откусываем поменьше
    a -= 1

# наполним кусок, который вырезали.. ну логично
result = [[1 for i in range(a)] for j in range(a)]
left -= a**2

# пока осталось чем, накладываем на стороны "куска"
while left > 0:
    result.append([])
    ilast = len(result) - 1
    for i in range(a):
        if left <= 0:
            break
        result[i].append(1)
        result[ilast].append(1)
        left -= 2

# ну и печатаем как попало
result.reverse()
size = len(result)
print(size)
for col in result:
    for i in col:
        print('o', end='', sep='')
    for i in range(len(col),size):
        print('.', end='', sep='')
    print()
