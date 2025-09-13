N, M = map(int, input().split())
A = list(map(int, input().split()))

m_list = [x for x in range(1, M+1)]
cnt = 0

if M == 1 : print(N)

for i in range(N):
	if all(m in A for m in m_list):
		A.pop()
		cnt+=1
	else:
		print(cnt)
		exit()