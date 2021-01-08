# 有效的字母异位词

## 哈希表的应用

#java代码是利用26个字母的总表，遇见一个就加，另一个里面有就减


#// java
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        int[] alpha = new int[26];
        for(int i = 0; i< s.length(); i++) {
            alpha[s.charAt(i) - 'a'] ++;
            alpha[t.charAt(i) - 'a'] --;
        }
        for(int i=0;i<26;i++)
            if(alpha[i] != 0)
                return false;
        return true;
    }
}

# python是利用计数比较结果是否一样

# python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums1 = collections.Counter(s) 
        nums2 = collections.Counter(t)
        if nums1 == nums2:
            return True
        else:
            return False


