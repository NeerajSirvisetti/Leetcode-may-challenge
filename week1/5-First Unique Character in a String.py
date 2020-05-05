class Solution:
    def firstUniqChar(self, s: str) -> int:
        m=list(s)
        k=list(dict.fromkeys(m))
        print(k)
        for i in k:
            if s.count(i)==1:
                return s.index(i)
                break
        return -1
            
        
