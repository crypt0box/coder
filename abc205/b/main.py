# !/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

sorted_a = sorted(A)

for i in range(1, N+1):
	if i == sorted_a[i-1]: continue
	else:
		print("No")
		exit()

print("Yes")