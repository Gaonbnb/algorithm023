def helper(s, left, right):
            if left == right == n:
                res.append(s)
            if left < n: helper(s+"(", left + 1, right)
            if left > right: helper(s+")", left, right + 1)
        res = []
        helper("", 0, 0)
        return res