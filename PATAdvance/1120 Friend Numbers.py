input()
arr = [sum([int(y) for y in str(x)]) for x in input().strip().split()]
arr = [str(x) for x in sorted(list(set(arr)))]
print(len(arr))
print(" ".join(arr))
