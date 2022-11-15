# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-15 19:32:00
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-15 19:39:40

x = input()
x = sum([int(x[i]) * 2**(i) for i in range(len(x))])
c = 0
i = 1
while True:
	if 2**i < x:
		i += 1
	else:
		if 2**(i-1) == x:
			c += 1
			break
		else:
			x -= 2**(i-1)
			c += 1
			i = 1

print(c)