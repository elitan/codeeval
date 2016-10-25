import fileinput

for line in fileinput.input():
	line = line.rstrip()
	x, y, n = list(map(int, line.split(' ')))
	for i in range(1, n+1):
		if i % x == 0 and i % y == 0:
			print("FB ", end="")
		elif i % x == 0:
			print("F ", end="")
		elif i % y == 0:
			print("B ", end="")
		else:
			print("{} ".format(i), end="")
	print("")
