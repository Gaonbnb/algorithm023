class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1. loop 数零的个数 双循环
        #2. 开一个新的数组，碰到0向后放，碰到非0向前放
        #3. index方法
        # length = len(nums)
        # nums_2 = [0] * length
        
        # next_node = 0
        # last_node = length - 1
        # for i in range(length):
           
        #     if nums[i] == 0:
                
        #         nums_2[last_node] = 0
                
        #         last_node -= 1
        #     else:
        #         nums_2[next_node] = nums[i]
                
        #         next_node += 1
        # nums = nums_2
        # print(nums)
        # 实际运用中是可行的，就是不能拷贝数组
        # 快捷键 ctrl+/

        # 两次遍历
        # if not nums:
        #     return 0
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[j] = nums[i]
        #         j += 1

        # for i in range(j, len(nums)):
        #     nums[i] = 0
        
        # 一次遍历 快速排序的思想
        # if not nums:
        #     return 0

        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j += 1


        if not nums:
            return None
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums