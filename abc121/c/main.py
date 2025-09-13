# !/usr/bin/env python3

from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(int)
ans = 0

for i in range(N):
	A, B = map(int, input().split())
	d[A] += B

sort_d = sorted(d.items(), key=lambda x:x[0])

for x in sort_d:
	if M - x[1] > 0:
		ans += x[0] * x[1]
		M -= x[1]
	else:
		ans += x[0] * M
		break

print(ans)