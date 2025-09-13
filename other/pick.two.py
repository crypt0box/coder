S = input()
ans = []

for i, s in enumerate(S):
	if s == "#":
		ans.append(str(i+1))
		if len(ans) == 2:
			print(",".join(ans))
			ans = []
