
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 网友的迭代stack
        # white, grey = 0, 1
        # res = []
        # stack = [(white, root)]
        # while stack:
        #     color, node = stack.pop()
        #     if node is None: continue
        #     if color == white:
        #         stack.append((white, node.right))
        #         stack.append((white, node.left))
        #         stack.append((grey, node))
        #     else:
        #         res.append(node.val)
        # return res
        # 递归方法
        res = []
        self.helptraversal(res, root)
        return res
    def helptraversal(self, res, root):
        if root:
            res.append(root.val)
            self.helptraversal(res, root.left)
            self.helptraversal(res, root.right)

