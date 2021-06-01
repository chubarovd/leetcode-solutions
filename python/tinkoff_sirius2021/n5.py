class Node:
    nexts = []
    def __init__(self, r, l):
        self.l = l
        self.r = r

    def insert(self, nd):
        if l + 1 == nd.r:
            self.nexts.append(nd)
            return True
        for n in self.nexts:
            if n.insert(nd):
                return True
        return False

    def walk(self, lim):
        max = self.l
        for nd in self.nexts:
            max = max(max, nd.walk(lim))
        return max

lim = int(input())

roots = []
pair = input().split(' ')
l = int(pair[0])
r = int(pair[1])
roots.append(Node(r, l))

while not (r == 0 and l == 0):
    pair = input().split(' ')
    l = int(pair[0])
    r = int(pair[1])
    inserted = False
    for root in roots:
        inserted = root.insert(Node(r, l))
    if not inserted:
        roots.append(Node(r, l))

for root in roots:
    print(root.walk(lim))