class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_at = {}
        best, start = 0, 0
        for i, char in enumerate(s):
            if char in last_seen_at and start <= last_seen_at[char]:
                start = last_seen_at[char] + 1
            else:
                best = max(best, i - start + 1)
            last_seen_at[char] = i
        return best
