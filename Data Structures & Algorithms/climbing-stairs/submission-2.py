class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        fib = [0] * (n+1)
        fib[1], fib[2] = 1, 2
        for i in range(3, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[-1]