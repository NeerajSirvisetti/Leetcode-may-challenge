class Solution:
    def findComplement(self, num: int) -> int:
        b= (bin(num)[2:] )
        b=b.replace("1","4")
        b=b.replace("0","1")
        b=b.replace("4","0")
        return int(b,2)