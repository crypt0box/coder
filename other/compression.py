N = int(input())
A = list(map(int, input().split()))

ans = sorted(set(A))

print(len(ans))
print(*ans)