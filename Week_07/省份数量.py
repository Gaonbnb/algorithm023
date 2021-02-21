class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 并查集
        if not isConnected: return 0
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.__union(p, i, j)
        return len(set(self.__parent(p, i) for i in range(n)))
    def __union(self, p, i, j):
        p1 = self.__parent(p, i)
        p2 = self.__parent(p, j)
        p[p2] = p1
    
    def __parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]

        # 下面是状态压缩的代码
        while p[i] != i:
            x = i; i = p[i]; p[x] = root
        return root