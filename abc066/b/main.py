# !/usr/bin/env python3

S = input()

for i in range(len(S)):
	even_s = S[:len(S)-i-1]
	if even_s[:len(even_s) // 2] * 2 == even_s:
		print(len(even_s))
		exit()
