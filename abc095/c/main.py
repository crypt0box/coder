# !/usr/bin/env python3

A, B, C, X, Y = map(int, input().split())
Z = A * (X - Y) if X > Y else B * (Y - X)

print(min(A * X + B * Y, min(X, Y) * 2 * C + Z, max(X, Y) * 2 * C))