
# pyhton 暴力法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j]
                if k == target:
                    return [i, j]

# hash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for index, num in enumerate(nums):
            if d.get(num) == None:
                d[target - num] = index
            else:
                return [d.get(num), index]
        # 哈希的第二版
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if target - nums[i] in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]


