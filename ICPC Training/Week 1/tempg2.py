# import sys
# sys.setrecursionlimit(1500)


def dp(a1,a2,p1,p2, dp_arr):
    if dp_arr[p1][p2] != -1:
        return dp_arr[p1][p2]
    if p1 == len(a1) or p2 == len(a2):
        dp_arr[p1][p2] = 0
        return 0
    if a1[p1] == a2[p2]:
        dp_arr[p1][p2] = 1 + dp(a1,a2,p1+1,p2+1,dp_arr)
        return dp_arr[p1][p2]
        # return 1 + dp(a1,a2,p1+1,p2+1,dp_arr)
    else:
        dp_arr[p1][p2] = max(dp(a1,a2,p1+1,p2,dp_arr),dp(a1,a2,p1,p2+1,dp_arr))
        return dp_arr[p1][p2]
        # return max(dp(a1,a2,p1+1,p2,dp_arr),dp(a1,a2,p1,p2+1,dp_arr))

# for i in range(int(input())):
#     input()
#     arr1 = [int(x) for x in input().strip().split()]
#     arr2 = [int(x) for x in input().strip().split()]
    

#     dp_arr = [[-1 for i in range(max(len(arr1), len(arr2))+1)] for j in range(max(len(arr1), len(arr2))+1)]


#     print(f"Case {i+1}: {dp(arr1,arr2,0,0,dp_arr)}")


from random import randint as ri
arr1 = list(set([ri(100, 1000) for i in range(1000)]))
arr2 = list(set([ri(100, 1000) for i in range(1000)]))
print(arr1)
print(arr2)
dp_arr = [[-1 for i in range(max(len(arr1), len(arr2))+1)] for j in range(max(len(arr1), len(arr2))+1)]
print(dp(arr1,arr2,0,0, dp_arr))
