def defaultDictCount(arr):
    dic = {}
    for x in arr:
        try:
            dic[x] += 1
        except:
            dic[x] = 1
    return dic    

def solution(files):
    y = defaultDictCount(files).values()
    return sum([z//2 for z in y])*2 + int(len([x for x in y if x %2 == 1]) >= 1)
    


# def main():
#     str = input()
#     answer = solution(str)
#     print(answer)


# if __name__ == '__main__':
#     main()

print(solution("abccccdd"))
print(solution("abzccccdd"))
print(solution("abzcccdd"))
print(solution("a"))