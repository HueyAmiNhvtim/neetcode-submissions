# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visiting = deque()
        visiting.appendleft((p, q))

        while visiting:
            node_p, node_q = visiting.popleft()
            if not node_p and not node_q:
                continue # Both None
            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            visiting.appendleft((node_p.left, node_q.left))
            visiting.appendleft((node_p.right, node_q.right))

        return True