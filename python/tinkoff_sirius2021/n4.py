n = int(input())
a = reversed(list(map(int, input().split())))

res = [0 for i in range(n)]

curr = 1
for ai in a:
    empty_left = ai
    for i in range(n):
        if empty_left == 0 and res[i] == 0:
            res[i] = curr
            break
        elif empty_left > 0 and res[i] == 0:
            empty_left -= 1
    #print(res, ai)
    curr += 1

print(" ".join(map(str, res)))

curr = 1
for k in a:
    j = 0
    for i in range(n):
      if res[i] == 0:
        if j == k:
          res[i] = curr
          break
        else:
          j += 1
    curr += 1
print(" ".join(map(str, res)))