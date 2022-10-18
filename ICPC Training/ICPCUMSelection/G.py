def monthList(year):
	if year%4 == 0:
		if year%100 == 0:
			if year%400 == 0:
				plus_1 = True
			else:
				plus_1 = False
		else:
			plus_1 = True
	else:
		plus_1 = False
	
	if plus_1:
		month = [31,29,31,30,31,30,31,31,30,31,30,31]	
	else:
		month = [31,28,31,30,31,30,31,31,30,31,30,31]
	return month

def day13Cumulative(year):
	arr = monthList(year)
	day = [13]
	for i in range(1,len(arr)):
		day.append(day[-1] + arr[i-1])
	return day,sum(arr)

def func(n):
	arr = [1900 + i for i in range(n)]
	arr2 = [day13Cumulative(x) for x in arr]
	counter = [0 for i in range(7)]
	t = 0
	for i in range(len(arr2)):
		if i == 0:
			for m in [(z)%7 for z in arr2[i][0]]:
				counter[m] += 1
			t += arr2[0][1]
		else:
			for m in [(z+t)%7 for z in arr2[i][0]]:
				counter[m] += 1
			t += arr2[i-1][1]
	return counter
print(func(20))










# ###################################################################################################################################################################################################
# # Encode: 0 -> Sun, 1 -> Mon
# # def day13th(one_at):
# 	# return (one_at + 12) % 7

# def monthList(year):
# 	if year%4 == 0:
# 		if year%100 == 0:
# 			if year%400 == 0:
# 				plus_1 = True
# 			else:
# 				plus_1 = False
# 		else:
# 			plus_1 = True
# 	else:
# 		plus_1 = False
	
# 	if plus_1:
# 		month = [31,29,31,30,31,30,31,31,30,31,30,31]	
# 	else:
# 		month = [31,28,31,30,31,30,31,31,30,31,30,31]
# 	return month

# # def firstDatInEachMonth(year):	
# # 	if year == 2022:
# # 		start = [6]
# # 	for x in monthList(year):
# # 		start.append((start[-1] + x) % 7)
	
# # 	day = [day13th(x) for x in start]
# # 	return day

# # def startDayOfTheYear(year):
# # 	if year == 1900:
# # 		return 1
# # 	else:
# # 		day = 1
# # 		for i in range(1900,year):
# # 			print(i)
# # 			day += sum(monthList(i-1))
# # 			day = day%7
# # 		return day

# # # print(startDayOfTheYear(1900))
# # # print(startDayOfTheYear(1901))
# # # print(startDayOfTheYear(2020))
# # # print(startDayOfTheYear(2021))
# # print(firstDatInEachMonth(2022))

# # print(monthList(2020))