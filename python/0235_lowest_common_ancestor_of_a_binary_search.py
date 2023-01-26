from common import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        small, big = sorted([p.val, q.val])
        while root:
            if small > root.val:
                root = root.right
            elif big < root.val:
                root = root.left
            else:
                return root
