COIN_ARRAY = [50,25,10,5,1]

def takeCoins(n,coin_arr,arr,cur_index=0):
    if cur_index == len(coin_arr) -1:
        return 1
    
    if arr[n][cur_index] != -1:
        return arr[n][cur_index]

    i = 0
    total = 0
    while n - i*coin_arr[cur_index] > 0:
        # print(i,n,coin_arr[cur_index], n-i*coin_arr[cur_index])
        total += takeCoins(n-i*coin_arr[cur_index], coin_arr,arr, cur_index+1)
        i+=1
    arr[n][cur_index] = total
    return total


arr = [[-1 for j in range(len(COIN_ARRAY)+1)] for i in range(7500)]
for i in range(int(input())):
    x = int(input())
    print(takeCoins(x,COIN_ARRAY,arr,0))

# 2
# 11
# 26