# !/usr/bin/env python3

N, Y = map(int, input().split())

for a in range(N+1):
	for b in range(N+1):
		if 9000 * a + 4000 * b + 1000 * N == Y and a >= 0 and b >= 0 and N - (a + b) >= 0:
			print(*[a, b, N - (a + b)])
			exit()

print(*[-1, -1, -1])