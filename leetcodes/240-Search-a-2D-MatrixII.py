class Solution:
    def searchMatrix(self, m, target):
        idxR, idxC = 0, len(m[0]) - 1
        while idxR < len(m) and idxC >= 0:
            if m[idxR][idxC] == target:
                return True

            if m[idxR][idxC] < target:
                idxR += 1

            else:
                idxC -= 1

        return False


if __name__ == '__main__':
    sol = Solution()
    m, target = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5  # true
    print(f"res is {sol.searchMatrix(m,target)}")
    m, target = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 26  # true
    print(f"res is {sol.searchMatrix(m,target)}")
    m, target = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], -2  # false
    print(f"res is {sol.searchMatrix(m,target)}")
    m, target = [[-5]], -5  # true
    print(f"res is {sol.searchMatrix(m,target)}")
