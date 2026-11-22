from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both null => same
        if p is None and q is None:
            return True
        
        # one null, one not => different
        if p is None or q is None:
            return False
        
        # values differ => different
        if p.val != q.val:
            return False
        
        # compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)