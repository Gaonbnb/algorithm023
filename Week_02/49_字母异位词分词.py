
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mp = collections.defaultdict(list)
        # # 遇到没有的key不会报错会返回一个空的list
        # # 里面存储的是list的类型
        # # 工厂函数
        # for st in strs:
        #     key = "".join(sorted(st))
        #     mp[key].append(st)
        
        # return list(mp.values())
        # mp = collections.defaultdict(list)
        # for st in strs:
        #     counts = [0] * 26
        #     for ch in st:
        #         counts[ord(ch) - ord("a")] += 1
        #     # 需要将 list 转换成 tuple 才能进行哈希
        #     mp[tuple(counts)].append(st)
        
        # return list(mp.values())
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch)-ord("a")] += 1
            mp[tuple(counts)].append(st)
        return list(mp.values())

