X, Y = map(int, input().split())
ans = []

for i in range(1,7):
	for j in range(1,7):
		if i + j >= X or abs(i-j) >= Y:
			ans.append([i, j])

result = [x for x in set(map(tuple, ans))]
print(len(result) / 36)