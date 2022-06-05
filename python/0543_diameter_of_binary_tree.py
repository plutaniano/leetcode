class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def walk(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left = self.walk(root.left)
        right = self.walk(root.right)

        self.diameter = max(left + right, self.diameter)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.walk(root)
        return self.diameter
