# 并查集
        def getIndex(i, j):
            return i * n + j
        if len(board) <= 1 or len(board[0]) <= 1: return board
        m, n = len(board), len(board[0])
        count = m * n
        self.node = count 
        p = [i for i in range(count + 1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    edge = (i == 0 or j == 0 or i == m - 1 or j == n - 1)
                    if edge and board[i][j] == "O":
                        self.union(p, getIndex(i, j), self.node)
                    else:
                        if i < m - 1 and board[i+1][j] =="O":
                            self.union(p, getIndex(i, j), getIndex(i+1, j))
                        if i > 0 and board[i-1][j] == "O":
                            self.union(p, getIndex(i, j), getIndex(i-1, j))
                        if j  < m - 1 and board[i][j+1] =="O":
                            self.union(p, getIndex(i, j), getIndex(i, j+1))
                        if j  > 0 and board[i][j-1] == "O":
                            self.union(p, getIndex(i, j), getIndex(i, j-1))
        for i in range(m):
            for j in range(n):
                if self.isConnected(p, getIndex(i, j), self.node):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board