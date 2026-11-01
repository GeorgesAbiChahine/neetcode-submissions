class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        temp = float('-inf')

        def inOrder(root):
            nonlocal temp

            if root is None:
                return True

            if not inOrder(root.left):
                return False

            if root.val <= temp:
                return False

            temp = root.val

            if not inOrder(root.right):
                return False

            return True

        return inOrder(root)