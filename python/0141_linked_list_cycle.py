from common import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """
        This version is very fast and consumes little memory,
        but destroys all the values in the list. Since LeetCode
        doesn't care if we preserve the list or not, this is
        probably the "best" option.
        """
        sentinel = object()
        slow = head
        while slow:
            if slow.val is sentinel:
                return True
            slow.val = sentinel
            slow = slow.next
        return False

    def hasCycle2(self, head: ListNode | None) -> bool:
        """This one is not as fast, but it preserves the list."""
        try:
            slow, fast = head, head.next
            while slow is not fast:
                fast = fast.next.next
                slow = slow.next
            return True

        except AttributeError:
            return False
