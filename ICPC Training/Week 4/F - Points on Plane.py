# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-15 19:41:13
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-15 20:22:40

import random

arr = []
for i in range(int(input())):
    arr.append([int(x) for x in input().strip().split() if x != ""])

dist = [[0 for __ in range(len(arr))] for _ in range(len(arr))]

for i in range(len(arr)):
	for j in range(len(arr)):
		x = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])
		dist[i][j] = x
		dist[j][i] = x

def greedy(d,s,v = [],c = 0):
	if c > 25*(10**8):
		return 26*(10**8)
	if len(v) == len(d):
		return v, c
	else:
		mi = None
		for j in range(len(d[s])):
			if j in v:
				continue
			else:
				if mi is None:
					mi = j
				else:
					if d[s][mi] > d[s][j]:
						mi = j
				v.append(mi)
				return greedy(d,mi,v, c + d[s][mi])

v = []
for _ in range(len(dist)-1):
	i = random.randint(0,len(dist)-1)

	while i in v:
		i = random.randint(0,len(dist)-1)
	v.append(i)
	# print(i)

	a,b = greedy(dist, i, [i])
	if b <= 25*(10**8):
		print(" ".join([str(a_+1) for a_ in a]))
		break