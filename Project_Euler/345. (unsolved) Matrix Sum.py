def subMat(mat, i, j):
    return [[mat[l][k] for k in range(len(mat[0])) if i != k] for l in range(len(mat)) if j != l]


def maxSum(mat, start_index_i, start_index_j, arr):
    if arr[start_index_i][start_index_j] != -1:
        return arr[start_index_i][start_index_j]

    if start_index_i == len():
        arr[start_index_i][start_index_j] = mat[0][0]
        return arr[start_index_i][start_index_j]

    maximum = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            maximum = max(
                maximum, mat[i][j] + maxSum(subMat(mat, i, j), start_index_i+1, start_index_j+1, arr))
    arr[start_index_i][start_index_j] = maximum
    return maximum


mat = \
    [[7, 53, 183, 439, 863],
     [497, 383, 563, 79, 973],
     [287, 63, 343, 169, 583],
     [627, 343, 773, 959, 943],
     [767, 473, 103, 699, 303]]

mat = \
    [[1, 2],
     [3, 4]]

mat = \
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

arr = [[-1 for _ in mat[0]] for _ in mat]

def matSum(mat,i,j):
	new_mat = subMat(mat,i,j)
	for i in range(len(mat)):
	    for j in range(len(mat[0])):
	        print(new_mat[i][j], subMat(new_mat, i, j))