class Solution:
    def __init__(self):
        self.diameter = 0
    
    def walk(self, root):
        if not root:
            return 0
        
        left = self.walk(root.left)
        right = self.walk(root.right)
        
        self.diameter = max(left + right, self.diameter)
        return 1 + max(left, right)
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.walk(root)
        return self.diameter
