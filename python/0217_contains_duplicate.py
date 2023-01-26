from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Iterative solution"""
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        Cool one-liner, but may take longer on some cases.

        nums = [1, 1, 2, 3, 4, ...]  # very big list

        If the duplicate number is on the start of the list,
        the iterative solution will return much faster since
        it won't need to add the rest of the list to the set.
        """
        return len(nums) != len(set(nums))
