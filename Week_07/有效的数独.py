row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        block = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    block_index = (i // 3) * 3 + j // 3
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    block[block_index][num] = block[block_index].get(num, 0) + 1
                    if row[i][num] > 1 or col[j][num] > 1 or block[block_index][num] > 1:
                        return False
        return True