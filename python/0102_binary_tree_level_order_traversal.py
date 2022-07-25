from common import TreeNode


class Solution:
    def as_iter(self, root: TreeNode):
        if not root:
            return
        current_nodes = [root]
        while current_nodes:
            yield [node.val for node in current_nodes]
            current_nodes = [
                getattr(n, side)
                for n in current_nodes
                for side in ["left", "right"]
                if getattr(n, side) is not None
            ]

    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        return list(self.as_iter(root))
