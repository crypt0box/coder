# !/usr/bin/env python3

c = [list(map(int, input().split())) for _ in range(3)]
a1 = 0
a2 = c[1][0] - c[0][0]
a3 = c[2][0] - c[0][0]
b1 = c[0][0]
b2 = c[0][1]
b3 = c[0][2]
a = [a1, a2, a3]
b = [b1, b2, b3]

for i in range(3):
	for j in range(3):
		if c[i][j] != a[i] + b[j]:
			print("No")
			exit()

print("Yes")