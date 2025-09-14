# !/usr/bin/env python3

N = int(input())
S = input()
ans = ""

for s in S:
	num = (ord(s) - ord("A") + N) % 26
	ans += chr(num + ord("A"))

print(ans)