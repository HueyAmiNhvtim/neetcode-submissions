class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for i in range(9)]
        # Check uniqueness in each row
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                    # Check uniqueness in each column
                    if board[i][j] in columns[j]:
                        return False
                    columns[j].add(board[i][j])

        # Now to check in 3x3 grid
        row_start, col_start = 0, 0
        while row_start != 9:
            while col_start != 9:
                grid_set = set()
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] != ".":
                            if board[i][j] in grid_set:
                                return False
                            grid_set.add(board[i][j])
                col_start += 3
            row_start += 3
        return True