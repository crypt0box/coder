N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
ans = 10**9
cnt = 0

# なぜこれで回転になるのかわかっていない
def rotate(S):
	return list(zip(*S[::-1]))

for i in range(4):
	for j in range(N):
		for k in range(N):
			if S[j][k] != T[j][k]:
				cnt+= 1
	ans = min(ans, i + cnt)
	S = rotate(S)
	cnt = 0

print(ans)