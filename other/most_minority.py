N, M = map(int, input().split())
S = [None] * N
for i in range(N):
	S[i] = input()
V = ["".join(x) for x in zip(*S)]
total = [0] * N

for m in range(M):
	cnt0 = 0
	cnt1 = 0
	if V[m].count("0") == N or V[m].count("1") == N:
		total = [x + 1 for x in total]
	for n in range(N):
		if V[m][n] == "0":
			cnt0 += 1
		else:
			cnt1 += 1
	if cnt0 < cnt1:
		for i, v in enumerate(V[m]):
			if v == "0":
				total[i] +=1
	else:
		for i, v in enumerate(V[m]):
			if v == "1":
				total[i] +=1
print(" ".join([str(i + 1) for i, x in enumerate(total) if x == max(total)]))