学习笔记

不同路径2
~~~
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        # 构造一个DP table
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0  # 如果第一个格子就是障碍，return 0
        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]

        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
~~~

最后一周了，继续学习了动态规划和字符串算法，动态规划应该是难度最大的算法题目了，感觉不是很好理解，动态规划就是一种带有记忆化的分治，中间记录着最优子问题的答案。首先分析动态规划问题的时候要分析最优子结构是怎么表示的，然后是每个dp的状态表示是什么，最后再写出状态转移方程，这个转移方程就依靠着最优子问题来进行书写。其中最难的状态转义方程比较难想出来。

接下来是字符穿的操作，首先是本身的一些操作和回文异位词等问题，这些都比较简单，但是只要碰上dp问题，立马难度就会高很多，这时候大多数情况是利用二维的dp进行问题的求解。