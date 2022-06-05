from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        letters = 0
        odd = False
        for count in counter.values():
            letters += (count // 2) * 2
            if not odd and count % 2 == 1:
                odd = True
        return letters + odd
