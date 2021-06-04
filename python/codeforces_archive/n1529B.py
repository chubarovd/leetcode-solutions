# https://codeforces.com/problemset/problem/1529/B

res = []
n = int(input())
for fake in range(n):
    k = int(input())
    arr = map(int, input().split(' '))
    arr = sorted(arr)
    k_max = 1
    if k > 1:
        min_d = abs(arr[1] - arr[0])
        for i in range(1, k):
            min_d = min(min_d, abs(arr[i] - arr[i - 1]))
            if arr[i] <= 0:
                k_max += 1
            elif arr[i] <= min_d:
                k_max += 1
            else:
                break
    res.append(k_max)

for r in res:
    print(r)
