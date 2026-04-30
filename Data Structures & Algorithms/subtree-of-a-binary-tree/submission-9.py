# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    # check if node and subRoot are the same
    def isSameTree(self, node, subRoot):
        if not node and not subRoot:
            return True
        if not node or not subRoot or node.val != subRoot.val:
            return False
        return self.isSameTree(node.left,subRoot.left) and self.isSameTree(node.right,subRoot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the subtree root
        stack = [root]
        node = None
        res = False
        while stack:
            node = stack.pop()
            if node and node.val == subRoot.val:
                res = res or self.isSameTree(node, subRoot)
            if node:
                stack.append(node.left)
                stack.append(node.right)
        
        return res