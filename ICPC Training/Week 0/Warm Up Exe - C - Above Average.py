for i in range(int(input())):
    arr = [int(x) for x in input().split()[1:]]
    count = 0
    for x in arr:
        if x > sum(arr)/len(arr):
            count += 1
    print(f"{count/len(arr)*100:.3f}%")


# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91