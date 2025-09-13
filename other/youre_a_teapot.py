S = input()
ans = 0

for i, ci in enumerate(S):
	if ci == "t":
		for j, cj in enumerate(S):
			if cj == "t" and i < j:
				t_and_t = S[i:j+1]
				if len(t_and_t) >= 3:
					ans = max(ans, (t_and_t.count("t") - 2) / (len(t_and_t) - 2))
print(ans)