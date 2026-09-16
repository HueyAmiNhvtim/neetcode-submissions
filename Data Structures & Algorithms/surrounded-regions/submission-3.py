from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        ROWS, COLS = len(board), len(board[0])
        
        visited = set()
        visiting = deque()  
        visiting.append((0, 0))
        
        while visiting:
            cur_row, cur_col = visiting.popleft()
            cur_val = board[cur_row][cur_col]
            
            if (cur_row, cur_col) not in visited:
                if cur_val == "O":
                    surrounded_os = []
                    visiting_o = deque()
                    visiting_o.append((cur_row, cur_col))
                    surrounded = True
                    
                    while visiting_o:
                        o_row, o_col = visiting_o.popleft()
                        if (o_row, o_col) not in visited:
                            surrounded_os.append((o_row, o_col))
                            # if O cell is at the border, then the whole patch is considered not surrounded
                            if (o_row == 0 or o_row == ROWS-1) or (o_col == 0 or o_col == COLS - 1):
                                surrounded = False

                            for direction in DIRECTIONS:
                                n_row, n_col = o_row + direction[0], o_col + direction[1]
                                if -1 < n_row < ROWS and -1 < n_col < COLS:
                                    n_val = board[n_row][n_col]
                                    if n_val not in visited:
                                        if n_val == "O":
                                            visiting_o.append((n_row, n_col))
                                        else:
                                            visiting.append((n_row, n_col))
                                        
                            visited.add((o_row, o_col)) 
                    if surrounded:
                        for o_row, o_col in surrounded_os:
                            board[o_row][o_col] = "X"
                else: # X, move as usuals
                    for direction in DIRECTIONS:
                        n_row, n_col = cur_row + direction[0], cur_col + direction[1]
                        if -1 < n_row < ROWS and -1 < n_col < COLS:
                                visiting.append((n_row, n_col))
                    visited.add((cur_row, cur_col))
                


            # Check if node is O.
            #   If true, then make a separate deque that tries to find all neighboring O's    