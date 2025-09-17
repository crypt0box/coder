# !/usr/bin/env python3

DX = [1, 1, 0, -1, -1, -1, 0, 1]
DY = [0, -1, -1, -1, 0, 1, 1, 1]

H, W = map(int, input().split())
S = [input() for _ in range(H)]

result = [[0 if v == "." else "#" for v in row] for row in S]

for i in range(H):
	for j in range(W):
		if S[i][j] == ".":
			continue

		for dx, dy in zip(DX, DY):
			ni, nj = i + dx, j + dy
			
			if ni < 0 or ni >= H or nj < 0 or nj >= W:
				continue
			
			if result[ni][nj] != "#":
				result[ni][nj] += 1

for row in result:
	print(*row, sep="")