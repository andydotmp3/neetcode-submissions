class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        # bfs starting at every treasure and going out towards land

        ROWS = range(len(grid))
        COLS = range(len(grid[0]))


        seen = set()
        queue = collections.deque()
        for row in ROWS:
            for col in COLS:
                if grid[row][col] != 0:
                    continue
                queue.append((row, col, 0))
                seen.add((row, col))

        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            row, col, val = queue.popleft()
            grid[row][col] = val
            for dr, dc in DIRECTIONS:
                new_row = row + dr
                new_col = col + dc
                if new_row not in ROWS or new_col not in COLS or (new_row, new_col) in seen or grid[new_row][new_col] in [0, -1]:
                    continue
                queue.append((new_row, new_col, min(val + 1, grid[new_row][new_col])))
                seen.add((new_row, new_col))
        

        
                    