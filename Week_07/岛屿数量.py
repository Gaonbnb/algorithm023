# 并查集
        def getIndex(i, j):
            return i * n + j
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        self.count = m * n
        water = 0
        parent = [i for i in range(self.count)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    water += 1
                else:
                    if i + 1 < m and grid[i+1][j] == "1":
                        self.union(parent, getIndex(i, j), getIndex(i+1, j))
                    if j + 1 < n and grid[i][j+1] == "1":
                        self.union(parent, getIndex(i, j), getIndex(i, j+1))
        return self.getcount() - water
    def union(self, parent, i, j):
        p1 = self.parent(parent, i)
        p2 = self.parent(parent, j)
        if p1 == p2: return 
        else:
            parent[p1] = p2
            self.count -= 1
    def parent(self, parent, i):
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != i:
            x = i; i = parent[i]; parent[x] = root
        return root
    def getcount(self):
        return self.count