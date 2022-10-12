def arrSimplified(arr):
    for i in range(len(arr)-1):
        if arr[i] >= 10:
            arr[i+1] += arr[i]//10
            arr[i] = arr[i] % 10

    while arr[-1] >= 10:
        arr.append(0)
        arr[-1] += arr[-2]//10
        arr[-2] = arr[-2] % 10
    return arr


arr = [1]
for i in range(1000):
    arr = [x*2 for x in arr]
    arr = arrSimplified(arr)
print(sum(arr))