n, x = map(int, input().split())
a = list(map(int, input().split()))

def search(x):
	l = 1
	r = n
	while (l <= r):
		m = (l + r) // 2
		if (x < a[m-1]): r = m - 1
		elif (x == a[m-1]): return m
		else: l = m + 1
	return -1

print(search(x))
