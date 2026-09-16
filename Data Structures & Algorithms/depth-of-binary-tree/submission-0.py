# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        visiting = deque()
        visiting.appendleft((1, root))
        max_depth = 0
        while visiting:
            node_depth, node = visiting.popleft()
            if max_depth < node_depth:
                max_depth = node_depth
                
            if node.left:
                visiting.appendleft((node_depth + 1, node.left))
            if node.right:
                visiting.appendleft((node_depth + 1, node.right))

        return max_depth