class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j=list(J)
        cnt=0
        s=list(set(S))
        for i in s:
            if i in j:
                cnt+=S.count(i)
        return (cnt)
        
