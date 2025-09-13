# !/usr/bin/env python3
A, B = map(int, input().split())

print(max(A+B, A-B, A*B))
