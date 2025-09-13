# !/usr/bin/env python3

N = int(input())
ans = []

def calc(n):
	cnt = 0
	while n % 2 == 0:
		n //= 2
		cnt += 1
	return cnt 


for i in range(1, N+1):
	ans.append(calc(i))

print(ans.index(max(ans)) + 1)