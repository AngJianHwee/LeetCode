
def pprint(*args):
	print("--", end = " ")
	[print(x, end = " ") for x in args]
	print()


for i in range(int(input())):
	input()
    arr = [int(x) for x in input().strip().split() if x != ""]

    

	dic = {}
	for x,y in arr:
	    try:
	        dic[x] += 1
	        dic[x] += y
	    except:
	        dic[x] = 1
	        dic[x] = y


######################################### SAMPLE INPUT ##################################