lim = int(input())
d = {}  # means dictionary :)
count = 0
for fake in range(0, lim):
    pair = input().split(' ')
    h = int(pair[0])
    w = int(pair[1])
    dh = d.get(h)
    dw = d.get(w)

    if dh is None:
        d[h] = []
    else:
        count += len(dh)

    if dw is None:
        d[w] = []
    elif w != h:
        count += len(dw)
        for el in dw:
            if el == h:
                count -= 1

    d[h].append(w)
    if w != h:
        d[w].append(h)
print(count)
