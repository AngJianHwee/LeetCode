# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-15 20:40:54
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-15 21:49:54

n,m = [int(x) for x in input().strip().split()]

if m == 0:
	print(0,0)
elif m == 1:
	print(int(((m-n)*(m-n-1)/2)), int(((m-n)*(m-n-1)/2)))
elif n <= m:
	print(0,0)
else:
	p_per_g = n//m
	n_extra_group = n%m
	n_normal_group = m - n%m

	min_count = 0
	min_count += n_normal_group * (p_per_g*(p_per_g-1)/2)
	p_per_g += 1
	min_count += n_extra_group * (p_per_g*(p_per_g-1)/2)

	print(int(min_count), int(((m-n)*(m-n-1)/2)))