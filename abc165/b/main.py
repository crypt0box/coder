# !/usr/bin/env python3
import math

X = int(input())
saving = 100
cnt = 0

while saving < X:
	cnt += 1
	saving += saving // 100

print(cnt)