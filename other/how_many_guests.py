n, q = map(int, input().split())
a = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(q)]
s = [0] * (n+1)

for i in range(n):
	s[i+1] = s[i] + a[i]

for i in range(q):
	print(s[lr[i][1]] - s[lr[i][0]-1])
