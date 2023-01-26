from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        magazine = Counter(magazine)

        for letter, n in note.items():
            if magazine.get(letter, 0) < n:
                return False
        return True
