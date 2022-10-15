x, y   = [int(x) for x in input().strip().split()]

done = False
for i in range(x, y+1):
	if len([x for x in str(i)]) == len(set([x for x in str(i)])):
		print(i)
		done = True
		break
if not done:
	print(-1)

######################################### SAMPLE INPUT ##################################