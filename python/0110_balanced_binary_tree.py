from common import TreeNode


class Solution:
    def depth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == -1 or right == -1 or abs(right - left) > 1:
            return -1
        return 1 + max(right, left)

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.depth(root) != -1
