# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        i = 0
        slow, fast = head, head
        while fast:
            fast = fast.next
            if i % 2:
                slow = slow.next
            i += 1
        return slow
