class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = '0'
            q.append((r, c))
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == '0':
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1
        return islands