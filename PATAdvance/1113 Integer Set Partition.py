input()
arr = [int(x) for x in input().strip().split()]
#     if len(arr)%2 == 0:
#         n,m = len(arr)//2,len(arr)//2
#     else:
#         n,m = len(arr)//2,len(arr)//2+1
x = sorted(arr)
a = x[:len(x)//2]
b = x[len(x)//2:]

print(len(b) - len(a), sum(b) - sum(a))