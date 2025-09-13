N, K = map(int, input().split())
A = list(map(int, input().split()))
disp = 1

for i in range(N):
	disp *= A[i]
	if len(str(disp)) > K:
		disp = 1

print(disp)