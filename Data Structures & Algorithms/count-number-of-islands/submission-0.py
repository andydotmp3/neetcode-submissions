class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        """
        - iterate through grid until we find a 1 whose coordinates are NOT in seen
        - run BFS on that
        - keep going until we get to the end
        """

        seen = set()
        count = 0

        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            seen.add((row, col))

            DIRECTIONS = ([1, 0], [-1, 0], [0, -1], [0, 1])

            while len(queue) > 0:
                row, col = queue.popleft()
                for dr, dc in DIRECTIONS:
                    newRow = row + dr
                    newCol = col + dc
                    if newRow not in range(len(grid)) or newCol not in range(len(grid[0])):
                        continue
                    if grid[newRow][newCol] == "0" or (newRow, newCol) in seen:
                        continue
                    queue.append((newRow, newCol))
                    seen.add((newRow, newCol))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in seen:
                    continue
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1
        return count
