 #dfs
        # 集合是可变的
        bank = set(bank)
        min_count = len(bank) + 1
        change_map = {"A":"CGT", "C":"AGT", "G":"ACT", "T":"ACG"}
        
        def dfs(word, level , cur_bank):
            nonlocal min_count
            # terminor
            if level > min_count:
                return 
            if word == end:
                if level < min_count:
                    min_count = level
            if not cur_bank:
                return 
            # process
            for i, alpha in enumerate(word):
                for ch in change_map[alpha]:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word not in cur_bank:
                        continue
                    # drill down
                    cur_bank.remove(new_word)
                    dfs(new_word, level+1, cur_bank)
                    cur_bank.add(new_word)
        dfs(start, 0, bank)
        return min_count if min_count <= len(bank) else -1