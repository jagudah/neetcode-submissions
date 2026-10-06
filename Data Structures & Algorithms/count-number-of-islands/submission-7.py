class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = '0'
            while q:
                qr, qc = q.pop()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] != '1':
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1
        return islands