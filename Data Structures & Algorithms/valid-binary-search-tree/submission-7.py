# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left_bound, right_bound):
            if not node:
                return True
            if not (node.val>left_bound and node.val<right_bound):
                return False
            return isValid(node.left,left_bound,node.val) and isValid(node.right,node.val,right_bound)
        return isValid(root,float('-inf'),float('inf'))
                
