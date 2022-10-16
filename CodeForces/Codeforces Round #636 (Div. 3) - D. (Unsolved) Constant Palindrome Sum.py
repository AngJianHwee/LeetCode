for i in range(int(input())):
    n, k = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]

    dic = {}
    for i in range(n//2):
        x = arr[i] + arr[n-i-1]
        try:
            dic[x] += 1
        except:
            dic[x] = 1
    print(dic)
    target_cs = [x for x in dic.keys() if dic[x] == max(list(dic.values()))]
    
    min_count = n
    for c in target_cs:
        count = 0
        for i in range(n//2):
            if (arr[i] + arr[n-i-1]) != c:
                if sorted([arr[i], arr[n-i-1]])[0] + c -  (arr[i] + arr[n-i-1]) < k:
                    count += 1
                else:
                    count += 2
        min_count = min(min_count,count)
    print("--",min_count)





######################################### SAMPLE INPUT ##################################
# 4
# 4 2
# 1 2 1 2
# 4 3
# 1 2 2 1
# 8 7
# 6 1 1 7 6 3 4 6
# 6 6
# 5 2 6 1 3 4
