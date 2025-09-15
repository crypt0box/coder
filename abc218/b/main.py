# !/usr/bin/env python3

P = list(map(int, input().split()))
ans = []

for p in P:
	ans.append(chr(p + ord("a") - 1))

print("".join(ans))