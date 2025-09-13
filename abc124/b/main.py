# !/usr/bin/env python3

N = int(input())
H = list(map(int, input().split()))

maxH = H[0]
cnt = 1

for i in range(1, N):
	if H[i] >= maxH:
		cnt += 1
		maxH = H[i]

print(cnt)