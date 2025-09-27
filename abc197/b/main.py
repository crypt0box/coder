# !/usr/bin/env python3

H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
cnt = 0

up = X - 1
while up >= 0 and S[up][Y-1] == ".":
	cnt += 1
	up -= 1

down = X - 1
while down < H and S[down][Y-1] == ".":
	cnt += 1
	down += 1

left = Y - 1
while left >= 0 and S[X-1][left] == ".":
	cnt += 1
	left -= 1

right = Y - 1
while right < W and S[X-1][right] == ".":
	cnt += 1
	right += 1


print(cnt-3)