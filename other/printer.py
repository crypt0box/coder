n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(x):
	sum = 0
	for i in range(n):
		sum += x // a[i]
	return sum >= k

left = 1
right = 10 ** 9

while left < right:
	middle = (left + right) // 2
	ans = check(middle)
	if ans:
		right = middle
	else: 
		left = middle + 1

print(right) 