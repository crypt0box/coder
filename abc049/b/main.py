# !/usr/bin/env python3

H, W = map(int, input().split())
C = [input() for _ in range(H)]
ans = [[None] * W for _ in range(2*H)]

for i in range(2*H):
	for j in range(W):
		ans[i][j] = C[(i)//2][j]

for s in ans:
	print("".join(s))