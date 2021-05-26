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
        d[h] = {0: 1}
    else:
        count += d[h][0]
        d[h][0] += 1

    if dw is None:
        d[w] = {0: 1}
    elif w != h:
        count += dw[0]
        dw[0] += 1

    if d[h].get(w) is None:
        d[h][w] = 1
    else:
        d[h][w] += 1
    if w != h:
        if d[w].get(h) is None:
            d[w][h] = 1
        else:
            count -= d[w][h]
            d[w][h] += 1
print(count)
