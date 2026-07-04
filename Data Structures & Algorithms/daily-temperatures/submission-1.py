class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 1
        tempsNum = len(temperatures)
        days = [0] * tempsNum

        while l < tempsNum - 1:
            if temperatures[l] < temperatures[r]:
                days[l] = r-l
                l += 1
                r = l + 1
            else:
                r += 1

            if r == tempsNum:
                days[l] = 0
                l += 1
                r = l + 1
        
        return days