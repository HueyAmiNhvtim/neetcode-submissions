class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False

        potential_path = deque()
        # Add the initial state
        for i in range(len(board)*len(board[0])):
            row = i % len(board)
            col = i // len(board)
            # Only add starting points that match the first letter of the word (prevent unnecessary path)
            if board[row][col] == word[0]:
                potential_path.appendleft(([(row, col)], 0)) # Store the current row and col
            # Assume that the order can be from up to down and left to right or reverse, so long as letter relative
            # position is maintained.

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, down, left, right
        while potential_path:
            paths, cur_i = potential_path.popleft()
            cur_r, cur_c = paths[-1][0], paths[-1][1]
            if cur_i == len(word) - 1: # Found the word in the board
                print(f"Path that matches the word {word}: {paths}")
                return True

            next_index = cur_i + 1
            for direction in directions:
                next_r, next_c = cur_r + direction[0], cur_c + direction[1]

                if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                    if board[next_r][next_c] == word[next_index] and (next_r, next_c) not in paths:
                        potential_path.appendleft((paths +[(next_r, next_c)], next_index))

        return False