# !/usr/bin/env python3

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = []

for h in H:
	ans.append(T - (h * 0.006))

c = [abs(x - A) for x in ans]

print(c.index(min(c)) + 1)