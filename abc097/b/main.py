# !/usr/bin/env python3

X = int(input())
bekis = [1]
ans = 0

for i in range(1,50):
	for j in range(2,10):
		bekis.append(i ** j)

for b in sorted(bekis):
	if b <= X:
		ans = b
		continue
	else:
		break

print(ans)