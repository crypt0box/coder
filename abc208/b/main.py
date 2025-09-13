# !/usr/bin/env python3
import math

P = int(input())
cnt = 0

for i in reversed(range(1, 11)):
	if P - math.factorial(i) < 0: continue
	else: 
		while P - math.factorial(i) >= 0:
			P -= math.factorial(i)
			cnt += 1

print(cnt)