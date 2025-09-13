# !/usr/bin/env python3

N = int(input())
save = 0
ans = 0

for i in range(1,N+1):
	save += i
	if save >= N: 
		ans = i
		break

print(ans)
