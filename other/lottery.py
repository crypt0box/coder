n = int(input())
a = list(map(int, input().split()))
q = int(input())
lr = [list(map(int,input().split())) for _ in range(q)]

sw = [0] * (n+1)
sl = [0] * (n+1)

for i in range(n):
	if a[i] == 1:
		sw[i+1] = sw[i] + 1
		sl[i+1] = sl[i]
	else:
		sw[i+1] = sw[i]
		sl[i+1] = sl[i] + 1 

for i in range(q):
	if sw[lr[i][1]] - sw[lr[i][0] - 1] > sl[lr[i][1]] - sl[lr[i][0] - 1]:
		print("win")
	elif sw[lr[i][1]] - sw[lr[i][0] - 1] == sl[lr[i][1]] - sl[lr[i][0] - 1]:
		print("draw")
	else:
		print("lose")
