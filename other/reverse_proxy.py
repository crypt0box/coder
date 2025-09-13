N, Q = map(int, input().split())
X = list(map(int, input().split()))
box = [0] * N
ans = []

for i in range(Q):
	if X[i] == 0:
		for j in range(len(box)):
			if box[j] == min(box):
				box[j] += 1
				ans.append(j+1)
				break
	else:
		box[X[i]-1] += 1
		ans.append(X[i])

print(*ans)