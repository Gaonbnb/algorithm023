# 回溯算法，中间的重置状态就是回溯的意思，也就是说下一层递归的状态在回到本层的时候对本层是不影响的，或者说是影响但是通过我自己的操作将这个影响消除了，所以中间都是同一个状态向着不同的下一层去进行递归的过程
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #版本一

        # def helper(n, index, cur_result):
        #     if index == n:
        #         res.append(cur_result[:])
        #         return
            
        #     for i in range(n):
        #         if nums[i] in cur_result:
        #             continue
        #         else:
        #             cur_result.append(nums[i])
                    
        #             helper(n, index+1, cur_result)
        #             cur_result.pop()
        # n = len(nums)
        # res = []
        # helper(n,0,[])
        # return res

        #官方题解用了一个新的数组存储是否使用
        def helper(n, index, cur_result):
            if index == n:
                res.append(cur_result[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                else:
                    cur_result.append(nums[i])
                    used[i] = True
                    helper(n, index+1, cur_result)
                    cur_result.pop()
                    used[i] = False
        n = len(nums)
        res = []
        used = [False] * n
        helper(n,0,[])
        return res