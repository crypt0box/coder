N = int(input())
S = [input() for _ in range(N)]
ans = []

for i in range(N):
	for j in range(N):
		if i != j:
			ans.append(S[i] + S[j])

print(len(set(ans)))