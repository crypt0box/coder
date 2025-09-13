N = int(input())
A = list(map(int, input().split()))

for i in reversed(range(N+1)):
	if [a >= i for a in A].count(True) >= i:
		print(i)
		exit()