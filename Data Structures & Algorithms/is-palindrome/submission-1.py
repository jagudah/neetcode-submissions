class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        sLower = s.lower()

        while l < r:
            if (sLower[l]).isalnum() is not True:
                l += 1
            elif (sLower[r]).isalnum() is not True:
                r -= 1
            else:
                if sLower[l] != sLower[r]:
                    return False
                l += 1
                r -= 1
        
        return True