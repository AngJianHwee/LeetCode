from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            arr = board[i]
            arr = [x for x in arr if x != "."]
            if len(arr) - len(list(set(arr))) != 0:
                return False
        for i in range(len(board)):
            arr = [x[i] for x in board]
            arr = [x for x in arr if x != "."]
            if len(arr) - len(list(set(arr))) != 0:
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                arr = []
                arr.extend(board[i][j:j+3])
                arr.extend(board[i+1][j:j+3])
                arr.extend(board[i+2][j:j+3])
                arr = [x for x in arr if x != "."]
                if len(arr) - len(list(set(arr))) != 0:
                    return False
        return True


s = Solution()
x = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(s.isValidSudoku(x))
x = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",                                                                                                                                                                                                  ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(s.isValidSudoku(x))


# # Model Solution
# def isValidSudoku(self, board):
#     return (self.is_row_valid(board) and
#             self.is_col_valid(board) and
#             self.is_square_valid(board))

# def is_row_valid(self, board):
#     for row in board:
#         if not self.is_unit_valid(row):
#             return False
#     return True

# def is_col_valid(self, board):
#     for col in zip(*board):
#         if not self.is_unit_valid(col):
#             return False
#     return True
    
# def is_square_valid(self, board):
#     for i in (0, 3, 6):
#         for j in (0, 3, 6):
#             square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#             if not self.is_unit_valid(square):
#                 return False
#     return True
    
# def is_unit_valid(self, unit):
#     unit = [i for i in unit if i != '.']
#     return len(set(unit)) == len(unit)