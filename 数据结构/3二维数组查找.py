'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
def findNumberIn2DArray(list,n):
    if n>list[-1][-1]:
        return None

    row = len(list)
    col = len(list[0])
    # print(row,col)
    for i in range(row):#######循环依次找
        for j in range(col):
            if n==list[i][j]:
                print(i,j)
                return True
    return None

def findNumberIn2DArray2(list,n):
    if n>list[-1][-1]:
        return None
    row = len(list)
    col = len(list[0])
    for i in range(row-1,-1,-1):#一行一行找
        if n>list[i][0]:
            for j in range(col):
                if n==list[i][j]:
                    print("row:%d,col:%d"%(i,j))
                    return True

#leetcode答题
# class Solution:
#     def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
#         row = len(matrix)
#         if row == 0:
#             return False
#         col = len(matrix[0])
#         if col == 0:
#             return False
#
#         if target > matrix[row - 1][col - 1]:
#             return False
#         i = row - 1
#         j = 0
#         while i >= 0 and j < col:
#             if target >= matrix[i][j]:
#                 if target == matrix[i][j]:
#                     return True
#                 else:
#                     j += 1
#             else:
#                 i -= 1
#         return False


print(findNumberIn2DArray2([[1,2,3,4,5],
                            [2,3,4,5,6],
                            [3,4,5,6,7],
                            [4,5,6,7,8],
                            [5,6,7,8,9]],
                    6))