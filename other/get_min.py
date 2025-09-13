Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
bag = []

for i in range(Q):
	if query[i][0] == 1:
		bag.append(query[i][1])
	else:
		print(min(bag))
		bag.remove(min(bag))