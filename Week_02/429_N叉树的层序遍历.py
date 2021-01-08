# 非递归
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            res.append(node.val for node in stack)
            stack = [child for node in stack for child in node.children]
        return res
        # 套上之后结果是二维的数组

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def traverse_node(root, level):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            for child in root.children:
                traverse_node(child, level + 1)
        result = []
        if root:
            traverse_node(root, 0)
        return result


