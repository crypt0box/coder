# !/usr/bin/env python3

N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

mod = X - sum(m)
cnt = 0

while True:
	mod -= min(m)
	if mod < 0: break
	cnt += 1

print(cnt + len(m))