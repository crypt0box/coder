import sys

N = int(input())
s = ""

for i in range(N):
	cl = list(map(str, input().split()))
	c, l = cl[0], int(cl[1])
	for j in range(l):
		s += c
		if len(s) > 100:
			print("Too Long")
			sys.exit()

print(s)