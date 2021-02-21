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
            for word in begin:
                for i in range(n):
                    for k in range(26):
                        new_word = word[:i] + chr(ord("a") + k) + word[i+1:]
                        if new_word in end:
                            return level
                        if new_word in wordList: # 写错了，比较重要
                            next_begin.add(new_word)
                            wordList.remove(new_word)
            begin = next_begin
            if len(begin) > len(end):
                begin, end = end, begin
        return 0