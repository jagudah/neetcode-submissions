class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []
        i = 0

        while i < len(temperatures):
            if len(stack) > 0 and stack[-1][1] < temperatures[i]:
                days[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            else:   
                stack.append((i, temperatures[i]))
                i += 1
        
        return days