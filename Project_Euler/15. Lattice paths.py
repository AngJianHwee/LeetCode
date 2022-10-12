def route(x1, y1, x2, y2, arr):
    if arr[x2-x1][y2-y1] != -1:
        return arr[x2-x1][y2-y1]
    if x1 == x2:
        return 1
    elif y1 == y2:
        return 1
    else:
        a = route(x1+1, y1, x2, y2, arr)
        b = route(x1, y1+1, x2, y2, arr)
        arr[x2-x1-1][y2-y1] = a
        arr[x2-x1][y2-y1-1] = b
        return a+b


N = 20
N += 1
print(route(1, 1, N, N, [[-1 for _ in range(N)] for _ in range(N)]))
