class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # step 1: look through the mins of the arrays. whichever is
        #  the closest without going over to the target is our destination array
        best_row_index = 0
        for i, row in enumerate(matrix):
            if row[0] <= target:
                best_row_index = i
        
        # now binary search through this
        best_row = matrix[best_row_index]
        left = 0
        right = len(best_row) - 1

        while left <= right:
            mid = (left + right) // 2
            if best_row[mid] == target:
                return True
            if best_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False