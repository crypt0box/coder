# !/usr/bin/env python3
from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
	S, T = input().split()
	t = int(T)
	d[S] = t

D = sorted(d.items(), key=lambda x: x[1])
print(D[-2][0])