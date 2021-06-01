def f(x, k, t):
    return x & ~((1 << k) - 1) | ((1 << k) - 1) * t


arg = input().split(' ')

l = int(arg[0])
r = int(arg[1])
x = int(arg[2])

k = 0
if l == x == r:
    k = 0
elif l == x != r:
    str = reversed(bin(x))
    for bit in str:
        if bit == '1':
            break
        else:
            k += 1
    k = min(k, len(bin(r - x)) - 2)
elif l != x == r:
    str = reversed(bin(x))
    for bit in str:
        if bit == 1:
            break
        else:
            k += 1
    k = min(k, len(bin(x - l)) - 2)
else:
    k = min(len(bin(x - l)), len(bin(r - x))) - 2
print(k, f(x, k, 0), f(x, k, 1))
