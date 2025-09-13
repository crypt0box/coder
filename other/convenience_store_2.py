t = int(input())
n = int(input())
l = [ None ] * n
r = [ None ] * n
for i in range(n):
	l[i], r[i] = map(int, input().split())

B = [0] * (t+1)

for i in range(n):
	B[l[i]] += 1
	B[r[i]] -= 1

ans = [0] * (t+1)

for i in range(0, t):
	ans[i] = ans[i-1] + B[i]

for i in range(t):
	print(ans[i])