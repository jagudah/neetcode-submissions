class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        digits_str = "".join(digits)
        res = int(digits_str) + 1
        res_str = str(res)
        return [int(digit) for digit in res_str]