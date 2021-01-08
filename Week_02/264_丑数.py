# 这种就用堆来做，堆里面可以是二叉堆，代替优先队列，就是优先级最高的也就是最大的在堆的顶部。


from heapq import heappop, heappush
class Ugly:
    def __init__(self):
        self.nums = nums = []
        seen = {1, }
        heap = []
        heappush(heap, 1)
        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]

