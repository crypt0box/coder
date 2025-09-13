X, Y = map(int, input().split())
ans = [ None ] * 10
ans[0] = X
ans[1] = Y

for i in range(2,10):
	ans[i] = int(str(ans[i-1] + ans[i-2])[::-1])

print(ans[-1])