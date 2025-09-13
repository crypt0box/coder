# !/usr/bin/env python3

K = int(input())
A, B = map(int, input().split())

a, b = 0, 0

for i in range(len(str(A))):
	a += (K ** i) * (A % 10)
	A //= 10
	
for i in range(len(str(B))):
	b += (K ** i) * (B % 10)
	B //= 10

print(a * b)