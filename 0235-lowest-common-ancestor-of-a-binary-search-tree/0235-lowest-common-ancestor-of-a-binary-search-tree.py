# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        elif p.val < root.val and q.val > root.val:
            return root
        elif p.val > root.val and q.val < root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        elif p.val > root.val and q.val > root.val: 
            root = root.right
            return self.lowestCommonAncestor(root, p, q)
        