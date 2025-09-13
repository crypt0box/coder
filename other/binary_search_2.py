def lower_bound(a, x):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l

n = int(input())
a = list(map(int, input().split()))
a.sort() 

q = int(input())
for _ in range(q):
    x = int(input())
    ans = lower_bound(a, x)
    print(ans)
