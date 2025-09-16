# !/usr/bin/env python3

a, b = map(int, input().split())
print(sorted([str(str(a) * b),str(a * str(b))])[0])