# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-11-15 20:07:11
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-11-15 20:08:27

s = input().strip()
p = input().strip()

def defaultDictCount(arr):
	dic = {}
	for x in arr:
		try:
			dic[x] += 1
		except:
			dic[x] = 1
	
	return dic

print(defaultDictCount((s)))
print(defaultDictCount((p)))