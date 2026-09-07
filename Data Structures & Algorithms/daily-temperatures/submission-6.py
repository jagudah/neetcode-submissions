class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, i = [], 0
        days = [0] * len(temperatures)

        while i < len(temperatures):                
            if len(stack) > 0 and temperatures[i] > stack[-1][-1]:
                days[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            else:
                stack.append((i, temperatures[i]))
                i += 1
        return days