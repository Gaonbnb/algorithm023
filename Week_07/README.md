学习笔记

这周学习的就是比较高级的数据结构和算法了，都是之前算法的加强版。主要是有并查集和字典树，对于并查集就是找一个点是否是同一个集合的结构，不过大部分都是同时可以用深度优先和广度优先遍历代替的，对于字典树就是用于存储字符型的树，便于查找。
对于单词搜索2的时间复杂度：我认为是这个时间复杂度O(M(4⋅3^L−1))，其中M是二维网格中的单元格数，L是单词的最大长度

之后是高级搜索的部分，这部分继承了之前的dfs和bfs，延伸出比如剪枝和双向bfs等算法，并且最后形成了启发式算法。
双向bfs有很多类似得部分
比如一开始得就是需要生成begin和end两个集合，然后while循环后面用的是begin and end.
```
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = set(wordList)
        begin = {beginWord}
        end = {endWord}
        level = 1
        n = len(beginWord)
        while begin and end:
            level += 1
            next_begin = set()
            """
            中间是不固定得部分
            for word in begin:
                for i in range(n):
                    for k in range(26):
                        new_word = word[:i] + chr(ord("a") + k) + word[i+1:]
                        if new_word in end:
                            return level
                        if new_word in wordList: # 写错了，比较重要
                            next_begin.add(new_word)
                            wordList.remove(new_word) # 这里是一个剪枝得部分会大幅度提高速度
            """
            # 下面是固定得
            begin = next_begin 
            if len(begin) > len(end):
                begin, end = end, begin
        return 0
```

最后是通过对二叉搜索树延伸出来的平衡二叉树的大概讲解，这个大概有AVL树和红黑树，都是比较难得算法，做一个大概的了解比较好。


