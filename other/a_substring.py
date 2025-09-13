N, A, B = map(int, input().split())
S = input()
subs = S[A:]
if B == 0:
	print(subs)
else:
	print(subs[:-B])