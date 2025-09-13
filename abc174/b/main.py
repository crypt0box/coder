# !/usr/bin/env python3
import math

N, D = map(int, input().split())
cnt = 0

for i in range(N):
	X, Y = map(int, input().split())
	d = math.sqrt(X ** 2 + Y ** 2)
	cnt += 1 if d <= D else 0

print(cnt)