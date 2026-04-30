# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deq = collections.deque()
        deq.append(root)
        res = []
        while deq:
            ln = len(deq)
            for _ in range(ln):
                node = deq.popleft()
                if node:
                    if node.left:deq.append(node.left)
                    if node.right:deq.append(node.right)
            if node:
                res.append(node.val)
        return res

