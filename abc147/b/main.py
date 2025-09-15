# !/usr/bin/env python3

S = input()
ans = 0

for i, s in enumerate(S[:len(S) // 2]):
	if s != S[-(i+1)]:
		ans += 1

print(ans)
