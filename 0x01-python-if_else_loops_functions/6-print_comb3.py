#!/usr/bin/python3
for i in range (0, 9):
	for j in range (0, 10):
		if i == 8 and j == 9:
			print("{:d}{:d}".format(i, j))
		elif i > j or (i == 0 and j == 0):
			pass
		else:
			print("{:d}{:d}, ".format(i, j), end= '')