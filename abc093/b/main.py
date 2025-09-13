# !/usr/bin/env python3

A, B, K = map(int, input().split())
ans = []

for i in range(K):
	if A+i > B: break
	ans.append(A+i)

for i in reversed(range(K)):
	if B-i < A: break
	ans.append(B-i)

for i in sorted(set(ans)):
	print(i)