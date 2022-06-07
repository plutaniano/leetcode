from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore Voting Algorithm"""
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

    def majorityElement2(self, nums: List[int]) -> int:
        target, d = len(nums) // 2, defaultdict(lambda: 0)
        for num in nums:
            d[num] += 1
            if d[num] > target:
                return num
