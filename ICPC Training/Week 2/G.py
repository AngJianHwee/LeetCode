a = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
for _ in range(int(input())):
	s = input()
	x = int(s[0:s.find("[")])
	# print("--", 1 x)
	y = s[s.find("[")+1:s.find("]")]
	print(f"Case #{_+1}: {100* (1 - (1000/1024)**(int(a.index(y)))):.2f}%")
