# !/usr/bin/env python3
from collections import defaultdict
import bisect

N, M = map(int, input().split())
d = defaultdict(list)
py = [map(int, input().split()) for _ in range(M)]
P, Y = [list(i) for i in zip(*py)]

for i in range(M):
	d[P[i]].append(Y[i]) 

for x in d.items():
	d[x[0]].sort()

for i in range(M):
	print('{:0=6}'.format(P[i]) + '{:0=6}'.format(bisect.bisect_left(d[P[i]],Y[i]) + 1))