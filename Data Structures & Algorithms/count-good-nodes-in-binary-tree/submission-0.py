# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return res
        stack = [[root,-101]]
        while stack:
            node,val = stack.pop()
            if node:
                if node.val >= val:
                    count+=1
                    val = node.val
                stack.append([node.left,val])
                stack.append([node.right,val])
        return count
        