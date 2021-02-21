class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.columns = set()
        self.pie = set()
        self.na = set()
        self.res = []
        self.helper(n, 0, [])
        return self.drawer(n)
    def helper(self, n, row, result):
        if n <= row:
            self.res.append(result)
            return 
        for col in range(n):
            if col in self.columns or row + col in self.pie or row - col in self.na:
                continue
            self.columns.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            self.helper(n, row+1, result + [col])
            self.columns.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)
    def drawer(self, n):
        bound = []
        for res in self.res:
            for i in res:
                bound.append("." * i + "Q" + "." * (n-i-1))
        return [bound[i:i+n] for i in range(0, len(bound), n)]