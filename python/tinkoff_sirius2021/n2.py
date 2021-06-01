s = input()
t = input()

counter = 0
n = len(s)
for i in range(n):
    if s[i] == t[i]:
        counter += 1

if counter == n:
    print(counter)
else:
    print(counter + 1)
