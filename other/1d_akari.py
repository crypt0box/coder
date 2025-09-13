S = input()
is_ok = True
T = ""

for s in S:
	if s == "#":
		is_ok = True
		T += "#"
	elif s == "." and is_ok:
		is_ok = False
		T += "o"
	else: T += "."

print(T)