# !/usr/bin/env python3

s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

print("Yes" if "".join(s) < "".join(t) else "No")