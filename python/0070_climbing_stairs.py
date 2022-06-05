cache = {1: 1, 2: 2}


class Solution:
    def climbStairs(self, n: int) -> int:
        """Recursive implementation with caching for massive speedup."""
        if n in cache:
            return cache[n]
        value = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        cache[n] = value
        return value
