# !/usr/bin/env python3
import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
	for j in range(i+1, N):
		s = 0
		for k in range(D):
			s += (X[i][k] - X[j][k]) ** 2
		if math.sqrt(s).is_integer():
			cnt += 1

print(cnt)