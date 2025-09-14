# !/usr/bin/env python3

A, B = map(int, input().split())
S = input()

for i in range(len(S)):
	if S[i] == "-" and i == A and S.count("-") == 1:
		print("Yes")
		exit()

print("No")