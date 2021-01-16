class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 从1跑完了之后就从2再开始跑
        def helper(n, index, result):
            if len(result) == k:
                res.append(result[:])
                return

             
            for i in range(index, n+1):
                result.append(i)
                
                helper(n, i+1, result)
                result.pop()
        
        res = []
        if k <= 0 or n < k: return res
        path = []
        helper(n, 1, path)
        return res
        # 下面是剪枝的操作
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 从1跑完了之后就从2再开始跑
        def helper(n, index, result):
            if len(result) == k:
                res.append(result[:])
                return

            # for i in range(index, n+1):
            # 这里是剪枝操作
            for i in range(index, (n - (k - len(result)) + 1)+1):
                result.append(i)
                
                helper(n, i+1, result)
                result.pop()
        
        res = []
        if k <= 0 or n < k: return res
        path = []
        helper(n, 1, path)
        return res        