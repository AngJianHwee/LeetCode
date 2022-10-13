for j in range(int(input())):
    high, low = 0, 0
    input()
    arr = [int(x) for x in input().split()]
   
    if len(arr) == 1:
        print(f"Case {j+1}: {high} {low}")
        continue

    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) == 0:
            continue
        elif (arr[i+1] - arr[i]) > 0:
            high += 1
        else:
            low += 1
    print(f"Case {j+1}: {high} {low}")



# 3
# 8
# 1 4 2 2 3 5 3 4
# 1
# 9
# 5
# 1 2 3 4 5