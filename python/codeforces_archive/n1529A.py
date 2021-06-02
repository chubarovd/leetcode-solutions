n = int(input())
ans = []

for fake in range(n):
    dct = {}
    min_ai = 101
    k = int(input())
    ais = list(map(int, input().split(' ')))
    for ai in ais:
        if ai < min_ai:
            min_ai = ai
        if dct.get(ai) is None:
            dct[ai] = 1
        else:
            dct[ai] += 1
    ans.append(k - dct[min_ai])

for a in ans:
    print(a)
