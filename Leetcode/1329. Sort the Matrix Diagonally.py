class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        new = mat.copy()
        m, n = len(mat), len(mat[0])
        i,j = 0,0
        arr = []
        for k in range(len(new)):
            try:
                arr.append(new[i+k][j+k])
            except:
                break
        arr = sorted(arr)
        for k in range(len(arr)):
            new[i+k][j+k] = arr[k]

        for i in range(1,m):
            j = 0
            arr = []
            for k in range(len(new)):
                try:
                    arr.append(new[i+k][j+k])
                except:
                    break
            arr = sorted(arr)
            for k in range(len(arr)):
                new[i+k][j+k] = arr[k]
            
        for j in range(1,n):
            i = 0
            arr = []
            for k in range(len(new)):
                try:
                    arr.append(new[i+k][j+k])
                except:
                    break
            arr = sorted(arr)
            for k in range(len(arr)):
                new[i+k][j+k] = arr[k]
            
        return new