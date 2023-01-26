from common import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """Recursive solution"""
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


# TODO: DFS, BFS solutions
