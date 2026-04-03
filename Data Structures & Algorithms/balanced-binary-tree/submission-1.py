# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)

        if abs(left_depth - right_depth) <= 1:
            from_left = self.isBalanced(root.left)
            from_right = self.isBalanced(root.right)
            return from_left and from_right
        else:
            return False
            

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)

        return 1 + max (left_depth, right_depth)
        