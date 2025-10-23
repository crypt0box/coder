# !/usr/bin/env python3
import math

A, B, _W = map(int, input().split())
W = _W * 1000
ans = []

for i in range(A, B + 1):
	for x in range(0, 1001):
		y = (W - A * x) / B
		if y.is_integer():
			ans.append([x, y])

print(ans[0])