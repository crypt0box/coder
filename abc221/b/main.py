# !/usr/bin/env python3

S = list(input())
T = input()

if "".join(S) == T:
    print("Yes")
    exit()

for i in range(len(S) - 1):
    S[i], S[i+1] = S[i+1], S[i]
    if "".join(S) == T:
        print("Yes")
        exit()
    S[i], S[i+1] = S[i+1], S[i]

print("No")