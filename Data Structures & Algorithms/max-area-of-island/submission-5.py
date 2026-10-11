class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        res = 0

        def bfs(r, c):
            nonlocal res
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            curr = 0
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + qr, dc + qc
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] != 1 or (nr, nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                curr += 1
            res = max(curr, res)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i, j)
        return res