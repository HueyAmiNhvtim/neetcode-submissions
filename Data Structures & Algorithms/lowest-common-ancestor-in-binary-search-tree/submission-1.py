# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visiting = deque()
        visiting.appendleft(root)

        while visiting:
            # When to stop....
            cur_node = visiting.popleft()
            # If the current node is equal to either p or q or it is bigger than one but smaller than the other
            # then it is a common ancestor
            if (cur_node.val == p.val or cur_node.val == q.val or p.val < cur_node.val < q.val or p.val > cur_node.val > q.val):
                return cur_node
            
            # If both nodes are bigger than the current node, go to the right
            if p.val > cur_node.val and q.val > cur_node.val:
                visiting.appendleft(cur_node.right)
            # If both nodes are smaller than the current node, go to the left
            if p.val < cur_node.val and q.val < cur_node.val:
                visiting.appendleft(cur_node.left)
            