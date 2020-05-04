Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true




ANS:


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        

        for i in ransomNote:
            if i in magazine:
                c=1
                magazine=magazine.replace(i,"",1)
            else:
                c=0
            if c==0:
                return False
        return True
