class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # Set of cells reachable from the pacific-adjacent cells and atlantic-adjacent cells, respectively

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                    r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    heights[r][c] < prevHeight
            ):
                return
            # When the cell has >= height compared to the prev-cell height (means from that cell,
            # flowing normally to the ocean is possible)
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start from the top and bottom row, performing reverse flow check
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Start from the left and right column, performing reverse flow check
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                # If a cell can flow to both oceans, it is a valid cell
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res  