k = int(input().strip())
S = input()
d = {}
for s in S:
	try:
		d[s] += 1
	except:
		d[s] = 1

done = False

for x, y in d.items():
	if y % k != 0:
		print(-1)
		done = True
		break

o = ''
if not done:

	for x, y in d.items():
		o += str(x)*(y//k)
	print(o*k)