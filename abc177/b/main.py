# !/usr/bin/env python3

S = input()
T = input()
ans = 0

if len(S) != len(T):
	for i in range(len(S) - len(T)):
		cnt = 0
		for j in range(i, len(T) + i):
			if S[j] == T[j-i]:
				cnt += 1
		ans = max(ans, cnt)
	print(len(T) - ans)
else:
	for i in range(len(S)):
		if S[i] != T[i]:
			ans += 1
	print(ans)