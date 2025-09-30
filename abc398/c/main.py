# !/usr/bin/env python3

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
ans = 0

candi = [i for i, x in c.items() if x == 1]

print(-1 if len(candi) == 0 else A.index(max(candi)) + 1)