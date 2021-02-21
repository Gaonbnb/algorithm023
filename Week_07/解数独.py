row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    block_index = (i // 3) * 3 + j // 3
                    row[i].remove(val)
                    col[j].remove(val)
                    block[block_index].remove(val)
                else:
                    empty.append((i, j))
        def backtrack(level=0):
            if level == len(empty):
                return True
            i, j = empty[level]
            b = (i // 3) * 3 + j // 3
            
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(level+1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()