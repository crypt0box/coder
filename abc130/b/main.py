# !/usr/bin/env python3

N, X = map(int, input().split())
L = list(map(int, input().split()))
b = [0]

for l in L:
	b.append(b[-1] + l)

print(len([x for x in b if x <= X]))