class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def bfs(r, c):
            nonlocal res
            curr = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0

            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] == 0:
                        res = max(curr, res)
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    curr += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    bfs(i, j)
        return res
