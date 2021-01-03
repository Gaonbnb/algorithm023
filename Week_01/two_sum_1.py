class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """k = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j]
                if k == target:
                    return [i, j]
        
        
        
        
        lens = len(nums)
        j=-1
        for i in range(lens):
            if (target - nums[i]) in nums:
                if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。&同1为1，且左右可以连接truefalse
                    continue
                else:
                    j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
                    break
        if j>0:
            return [i,j]
        else:
            return []
      

        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None 

        lens = len(nums)
        j=-1
        for i in range(1,lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j>=0:
            return [j,i]
        """
        # 反向存储
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        print
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]