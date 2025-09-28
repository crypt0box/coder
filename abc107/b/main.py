# !/usr/bin/env python3

H, W = map(int, input().split())
a = [input() for _ in range(H)]
row = []
col = []
ans = []

for i in range(H):
	cnt = 0
	for j in range(W):
		if a[i][j] == ".":
			cnt += 1
	if cnt == W:
		row.append(i)

a = [x for i, x in enumerate(a) if i not in row]

for i in range(len(a[0])):
	cnt = 0
	for j in range(len(a)):
		if a[j][i] == ".":
			cnt += 1
	if cnt == len(a):
		col.append(i)

for ch in a:
	moji = ""
	for i, c in enumerate(list(ch)):
		if i not in col:
			moji += c
	ans.append(moji)

for an in ans:
	print(an)