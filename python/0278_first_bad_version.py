def isBadVersion(*args, **kwargs):
    """Provided by the LC environment."""
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Basically binary search"""
        left, right = 1, n

        while left < right:
            middle = (left + right) // 2
            is_bad = isBadVersion(middle)

            if is_bad is False:
                left = middle + 1
            else:
                right = middle
        return left
