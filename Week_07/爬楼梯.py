# 用字典当作备忘录的递归写法

        self.dict_ = {1:1, 2:2}
        def recur(n):
            # 剪枝操作
            if n not in self.dict_:
                self.dict_[n] = recur(n-1) + recur(n-2)
            return self.dict_[n]
        return recur(n)