# !/usr/bin/env python3

s = input()
A, B, C, D = s[0], s[1], s[2], s[3]
ops = ["+", "-"]

for o1 in ops:
	for o2 in ops:
		for o3 in ops:
			expr = A + o1 + B + o2 + C + o3 + D
			if eval(expr) == 7:
				print(expr + "=7")
				exit()