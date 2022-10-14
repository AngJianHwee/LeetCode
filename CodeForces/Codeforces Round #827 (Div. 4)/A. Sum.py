for i in range(int(input())):
    arr = [int(x) for x in input().strip().split()]
    arr = sorted(arr)
    if arr[0]+arr[1] == arr[2]:
        print("YES")
    else:
        print("NO")