# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = collections.deque()
        deq.append(root)
        res = []
        while deq:
            l = []
            for i in range(len(deq)):
                node = deq.popleft()
                if node:
                    l.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
            if l:
                res.append(l)
        return res