def defaultDictCount(arr):
	dic = {}
	for x in arr:
		try:
			dic[x] += 1
		except:
			dic[x] = 1
	
	return [x%2 for x in dic.values()]

def state(s):
	x = defaultDictCount(s)
	if sum(x) < 2:
		return 1
	else:
		if sum(x) % 2 == 0:
			return 2
		else:
			return 1

s = input()
# s = "aba"
# s = "abca"
# s = "abcabz"
# s = "abzdce"
if state(s) == 1:
	print("First")
else:
	print("Second")
