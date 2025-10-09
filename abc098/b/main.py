# !/usr/bin/env python3

N = int(input())
S = input()

ans = 0

for i in range(1,N):
	cnt = 0
	for s in set(S[:i]):
		if s in set(S[i:]):
			cnt += 1
	ans = max(ans, cnt)

print(ans)