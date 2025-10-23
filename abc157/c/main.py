# !/usr/bin/env python3

N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]

for i in range(10 ** N):
	ch = str(i).zfill(N)
	
	if N >= 2 and ch[0] == "0": continue

	isOK = True
	for s, c in SC:
		if ch[s-1] != str(c):
			isOK = False
			break
	
	if isOK:
		print(ch)
		exit()

print(-1)