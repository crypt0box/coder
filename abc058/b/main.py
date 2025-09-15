# !/usr/bin/env python3

O = input()
E = input()
ans = ""

for i, e in enumerate(E):
	ans += O[i] + e

print(ans if len(O) == len(E) else ans + O[-1])
