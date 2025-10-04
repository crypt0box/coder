# !/usr/bin/env python3

N = int(input())
S = [input() for _ in range(N)]
_X, Y = input().split()
X = int(_X)

print("Yes" if S[X - 1] == Y else "No")