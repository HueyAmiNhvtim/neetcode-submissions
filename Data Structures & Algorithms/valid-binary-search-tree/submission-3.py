# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        visiting = deque()
        # Store
        visiting.appendleft((root, float("-inf"), float("+inf"))) # Store the node, the minimum value on the path so far, and the maximum number on the path so far
        while visiting:
            node, min_so_far, max_so_far = visiting.popleft()
            if node.left:
                if node.val > node.left.val > min_so_far:
                    visiting.appendleft((node.left, min_so_far , node.val))
                else:
                    return False
            if node.right:
                if node.val < node.right.val < max_so_far:
                    visiting.appendleft((node.right, node.val, max_so_far))
                else:
                    return False
                pass
        return True        