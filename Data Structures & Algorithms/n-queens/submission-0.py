from collections import deque
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []

        placements = []
        potential_solution = deque()
        # Add initial state. We know that since 2 queens
        # cannot be on the same row, that means to place an n
        # queen on an nxn board, all queens have to be on separate
        # rows, meaning that the initial states of placing the first
        # queen just only has to be on the first row of the board!
        # Subsequently, for each subsequent queen placement,
        # The next possible transition states can just be on a single row!
        # This prevents overlapping solution + reducing search space for a possible transition step!

        for i in range(n):
            potential_solution.appendleft([(0, i)])

        while potential_solution:
            placed_queens = potential_solution.popleft()
            if len(placed_queens) == n:
                placements.append(placed_queens)
            
            next_row = len(placed_queens)
            # Go through column at the next row
            for i in range(n):
                pot_pos = (next_row, i)
                overlapped = False
                for position in placed_queens:
                    # Check if the potential_position is not 
                    # in the fire range of any already placed queen
                    # We don't have to check for row
                    if i == position[1]: # Check for column overlapping
                        overlapped = True
                        break
                    # Check for diagonal overlapping
                    if abs(position[0]-next_row) == abs(position[1]-i):
                        overlapped = True
                        break

                if not overlapped:
                    potential_solution.appendleft((placed_queens + [pot_pos]))

        # Placing n queens on an nxn board
        # We can store the position of the queen 
        # From a position of the queen, for any position,
        # we can detect if that position can be reached by
        # the queen either vertically, horizontally, or 
        # diagonally.
        print(placements)
        # A solution is infeasible if there exists no possible 
        # space to fit a queen
        result = self.format_solution(placements, n)
        return result

    def format_solution(self, queen_placements: List, n):
        # Format the solution according to NeetCode output
        result = []
        for solution in queen_placements:
            board = [["." for _ in range(n)] for _ in range(n)]
            for placement in solution:
                row, col = placement
                board[row][col] = "Q"
            result.append(["".join(row) for row in board])
        return result

