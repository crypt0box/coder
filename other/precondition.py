S = input()
T = input()
ans = []

for i, c in enumerate(S):
	if i == 0: continue
	if c.isupper():
		ans.append(S[i-1])

is_ok = all(c in T for c in ans)
print("Yes" if is_ok else "No")