def solution(n, flows):
    arr = []
    f = flows
    for i in range(len(f)):
        s = i
        c = 1
        while i+1 != f[s]:
            c += 1
            s = (s+1)%len(f)
            # print(i,s,f[s],f)
        arr.append(c)
    print(" ".join([str(x) for x in arr]))
    


def main():
    n = int(input())
    flows = list(map(int, input().split()))
    solution(n, flows)


if __name__ == '__main__':
    main()

# flows = [2,3,1]
# flows = [1,2,3,4,5]
# solution(0, flows)
