class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        seen = set()

        
        max_count = 0
        def bfs(row, col):
            current_count = 1
            DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
            queue = collections.deque()
            seen.add((row, col))
            queue.append((row, col))
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in DIRECTIONS:
                    row_new = row + dr
                    col_new = col + dc

                    if row_new not in range(len(grid)) or col_new not in range(len(grid[0])) or (row_new, col_new) in seen or grid[row_new][col_new] == 0:
                        continue
                    current_count += 1
                    queue.append((row_new, col_new))
                    seen.add((row_new, col_new))
            
            return current_count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] == 1:
                    count = bfs(row, col)
                    if count > max_count:
                        max_count = count
        return max_count
