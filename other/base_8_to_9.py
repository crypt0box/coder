N, K = map(int, input().split())
ans = N

def calc(n):
	ans = 0
	result = ""
	for i in range(len(str(n))):
		ans += 8 ** i * (n % 10)
		n //= 10

	while ans != 0:
		result =  str(ans % 9) + result
		ans //= 9

	return int("0" if result == "" else result.replace("8", "5"))

for i in range(K):
	ans = calc(ans)

print(ans)