def subMat(mat, i, j):
    return [[mat[l][k] for k in range(len(mat[0])) if i != k] for l in range(len(mat)) if j != l]


mat = \
    [[7, 53, 183, 439, 863],
     [497, 383, 563, 79, 973],
     [287, 63, 343, 169, 583],
     [627, 343, 773, 959, 943],
     [767, 473, 103, 699, 303]]

# mat = \
#     [[1, 2],
#      [3, 4]]

# mat = \
#     [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# arr = [[-1 for _ in mat[0]] for _ in mat]


def matSum(mat):
    if len(mat) == 2:
        return max(mat[0][0] + mat[1][1], mat[1][0] + mat[0][1])

    print("Call")
    maximum = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            maximum = max(maximum, mat[i][j]+matSum(subMat(mat, i, j)))
    return maximum


print(matSum(mat))
