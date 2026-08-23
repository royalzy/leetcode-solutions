class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''' binary search'''
        if not matrix:
            return False

        rows = len(matrix) - 1
        columns = len(matrix[0]) - 1

        top, bot = 0, rows

        if matrix[-1][-1] < target:
            return False 

        while top <= bot:
            mid = ((top + bot) // 2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                bot = mid
                break
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bot = mid - 1

        l, r = 0, columns
        while l <= r:
            mid = ((l+r) // 2)
            if matrix[bot][mid] == target:
                return True
            elif matrix[bot][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

