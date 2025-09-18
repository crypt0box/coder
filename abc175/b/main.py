# !/usr/bin/env python3

N = int(input())
L = list(map(int, input().split()))
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                if L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:
                    ans += 1

print(ans)