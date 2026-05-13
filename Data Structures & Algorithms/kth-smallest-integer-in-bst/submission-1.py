# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return res[k-1]

        deq = []
        node = root
        res = 0
        while True:
            while node:
                deq.append(node)
                node = node.left
            node = deq.pop()
            res += 1
            if res == k:
                return node.val
            node = node.right
