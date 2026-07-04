class Solution:
    def isArmstrong(self, n: int) -> bool:
        nStr = str(n)
        K = len(nStr)

        for num in nStr:
            numInt = int(num)
            n -= pow(numInt, K)
        
        return n == 0