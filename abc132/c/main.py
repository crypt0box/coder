# !/usr/bin/env python3

N = int(input())
d = list(map(int, input().split()))

d.sort()

median = len(d) // 2

print(d[median] - d[median - 1])