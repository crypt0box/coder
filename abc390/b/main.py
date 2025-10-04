# !/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
flag = True

for i in range(N-2):
	if A[i] * A[i+2] != A[i+1] ** 2:
		flag = False

print("Yes" if flag else "No")