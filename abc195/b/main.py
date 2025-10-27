# !/usr/bin/env python3

A, B, _W = map(int, input().split())
W = _W * 1000

minN = (W + B - 1) // B
maxN = W // A

if minN > maxN:
    print("UNSATISFIABLE")
else:
    print(minN, maxN)