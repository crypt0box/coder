d = int(input())
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
l, r = [list(i) for i in zip(*lr)]

B = [0] * (d+2)

for i in range(n):
	B[l[i]] += 1
	B[r[i] + 1] -= 1

s = [0] * (d+1)

for i in range(1, d+1):
	s[i] = s[i-1] + B[i]

for i in range(1, d+1):
	print(s[i])