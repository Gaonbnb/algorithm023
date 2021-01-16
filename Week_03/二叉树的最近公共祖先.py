# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root == p or root == q:
            return root
        
        leftnum = self.lowestCommonAncestor(root.left, p, q)
        rightnum = self.lowestCommonAncestor(root.right, p, q)
        if not root and not leftnum and not rightnum:
            return None
        if not leftnum:
            return rightnum

        if not rightnum:
            return leftnum
        return root 
        