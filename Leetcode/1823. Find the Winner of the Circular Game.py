class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(n))
        prev = 0
        while len(arr) > 1:
            cur_i = (len(arr) + prev) % len(arr)
            cur_i += k-1
            cur_i = cur_i % len(arr)
            prev = cur_i
            arr = [arr[i] for i in range(len(arr)) if i != cur_i]
            # print(arr)
            # break
        return arr[0]+1


s = Solution()
print(s.findTheWinner(n=5, k=2))
print(s.findTheWinner(n=6, k=5))

# # Model Solution
# class Solution:
# def findTheWinner(self, n: int, k: int) -> int:
#     ls=list(range(1,n+1))
#     while len(ls)>1:
#         i=(k-1)%len(ls)
#         ls.pop(i)
#         ls=ls[i:]+ls[:i]
    
#     return ls[0]