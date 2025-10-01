# !/usr/bin/env python3

N = int(input())
ans = ""

for i in range(N):
	if i == N // 2 or i == (N - 1) // 2:
		ans += "="
	else:
		ans += "-"

print(ans)