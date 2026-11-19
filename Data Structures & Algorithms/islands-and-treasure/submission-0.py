class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        visited = set()
        land = pow(2,31) - 1
        dist = 0
        
        def addLand(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c] != land:
                return
            q.append([r, c])
            visited.add((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        while q:
            qLen = len(q)
            for i in range(qLen):
                qr, qc = q.popleft()
                grid[qr][qc] = dist
                for dr, dc in directions:
                    addLand(qr + dr, qc + dc)
            dist += 1