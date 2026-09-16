# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        visiting = deque()
        visiting.appendleft((root, 0))
        while visiting:
            node, level = visiting.popleft()
            if (level + 1) > (len(result)): # No rightmost node found at this level yet, then this one is here.
                result.append(node.val)
            # Go as right as possible.
            if node.left:
                visiting.appendleft((node.left, level+1))
            if node.right:
                visiting.appendleft((node.right, level+1))

        return result