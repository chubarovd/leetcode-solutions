lim = int(input())
lock = False
color = 'blue'
for fake in range(0, lim):
    line = input()
    if line == 'lock':
        lock = True
    elif line == 'unlock':
        lock = False
    elif not lock:
        color = line
print(color)
