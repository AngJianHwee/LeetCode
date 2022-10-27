for i in range(int(input())):
    input()
    arr1 = [int(x) for x in input().strip().split()]
    arr2 = [int(x) for x in input().strip().split()]
    
    p1 = 0
    p2 = 0
    s = []
    while p1 != len(arr1) and p2 != len(arr2):
        if arr1[p1] == arr2[p2]:
            s.append(arr1[p1])
        else:
            