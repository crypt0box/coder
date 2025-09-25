# !/usr/bin/env python3

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]
punched = [[None] * 3 for _ in range(3)]
ans = "No"

for i in range(3):
	for j in range(3):
		punched[i][j] = A[i][j] in b

for i in range(3):
	if punched[i][0] and punched[i][1] and punched[i][2]:
		ans = "Yes"

for i in range(3):
	if punched[0][i] and punched[1][i] and punched[2][i]:
		ans = "Yes"

if punched[0][0] and punched[1][1] and punched[2][2]:
	ans = "Yes"

if punched[0][2] and punched[1][1] and punched[2][0]:
	ans = "Yes"

print(ans)