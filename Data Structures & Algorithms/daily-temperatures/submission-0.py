class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        l = 0
        r = 1

        while l < len(temperatures) - 1:
            stack.append(temperatures[l])
            if temperatures[l] < temperatures[r]:
                res[l] = r-l
                l += 1
                r = l
            else:
                if (r == len(temperatures) - 1 and stack):
                    res[l] = 0
                    l += 1
                    r = l
            stack.pop()
            r += 1

        return res