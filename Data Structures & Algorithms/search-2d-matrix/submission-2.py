class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Look at the first element of each row first (column traversal), then go inside the row for proper binary search
        l_row, r_row = 0, len(matrix) - 1
        row_index = -1
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2
            if target < matrix[m_row][0]:
                r_row = m_row - 1
            elif target > matrix[m_row][-1]:
                l_row = m_row + 1
            else:
                row_index = m_row
                break

        if not(l_row <= r_row):
            return False

        # Now to do regular binary search inside the row
        return self.binary_search(matrix[row_index], target)

    def binary_search(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True
        return False