 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            root_preorder = preorder_left
            root_num = index[preorder[root_preorder]]
            root = TreeNode(inorder[root_num])
        
            left_length = root_num - inorder_left
            root.left = helper(preorder_left+1, preorder_left+left_length,inorder_left, root_num-1)
            root.right = helper(preorder_left+left_length+1, preorder_right, root_num+1, inorder_right)
            return root
        

        n = len(preorder)

        index = {element:i for i, element in enumerate(inorder)}
        return helper(0, n-1, 0, n-1)